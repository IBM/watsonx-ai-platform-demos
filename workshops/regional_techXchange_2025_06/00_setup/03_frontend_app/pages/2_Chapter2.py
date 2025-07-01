import os
import requests
import streamlit as st
from dotenv import load_dotenv
from utils.utils import init_db, get_credentials, save_credentials, display_configuration

def get_bearer_token(api_key):
    """
    Retrieve a Bearer token from IBM Cloud IAM.

    Args:
        api_key (str): IBM Cloud API key.

    Returns:
        str: Bearer token if successful, None otherwise.
    """
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": api_key
    }
    response = requests.post(url, headers=headers, data=data, verify=False)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Failed to retrieve token: {response.text}")
        return None

def display_results(results):
    """
    Display predictions and proximity search results in the Streamlit app.

    Args:
        results (dict): The response from the Watsonx deployment containing predictions.
    """
    generated_response = results['choices'][0]['message']['content']
    st.write(f"**Generated Response:**\n\n{generated_response}")



def display_page2():
    """
    Main function to display the second page of the Streamlit app,
    allowing users to input their API key, deployment URL, and generate a response.
    """
    st.title("IBM Watson Assistant - DB2 RAG Assistant")

    # Initialize database and load environment variables
    init_db()
    load_dotenv()

    # Get API key and deployment URL from configuration section
    api_key, deployment_url_write_email, deployment_url_rag = display_configuration("rag")
    deployment_url = deployment_url_rag

    # Default user question
    default_question = (
        "I'm trying to execute a routine named GET_CUSTOMER_DATA in DB2, but it "
        "returns an error: 'Routine not found in schema.' I double-checked the routine "
        "name, and it exists in the catalog."
    )
    user_question = st.text_area("Enter your question", value=default_question, height=150)

    # Prepare payload for scoring request
    payload_scoring = {
        "messages": [
            {
                "role": "user",
                "content": user_question
            }
        ]
    }

    # Button to generate an email
    if st.button("Query knowledge base"):
        with st.spinner("Sending request to IBM GenAI model..."):
            print ("sending request to:", deployment_url)
            try:
                response = requests.post(
                    deployment_url,
                    json=payload_scoring,
                    headers={"Authorization": f"Bearer {get_bearer_token(api_key)}"}
                )
                if response.status_code == 200:
                    try:
                        response_json = response.json()
                        display_results(response_json)
                    except requests.exceptions.JSONDecodeError as e:
                        st.error(f"Failed to parse response as JSON: {str(e)}")
                        st.write("Raw response:", response.text)
                else:
                    st.error(f"Request failed with status code {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    display_page2()
