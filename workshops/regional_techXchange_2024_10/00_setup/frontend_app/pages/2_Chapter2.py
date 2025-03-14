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
    predictions = results['predictions'][0]

    # Extract proximity search results and generated response
    proximity_results = predictions['values'][0]
    generated_response = predictions['values'][1]

    # Display the generated response
    st.write(f"**Generated Response:**\n\n{generated_response}")

    # Display proximity search results
    st.markdown("**Proximity Search Results:**")
    for result in proximity_results:
        metadata = result['metadata']
        score = result['score']
        st.write(f"Asset: {metadata['asset_name']} (Score: {score:.2f})")
        st.write(f"Range: {metadata['from']} - {metadata['to']}")
        # Uncomment the following line to display document links if available
        # st.write(f"[View Document]({metadata['url']})")
        st.write("---")  # Separator for readability

def display_page2():
    """
    Main function to display the second page of the Streamlit app,
    allowing users to input their API key, deployment URL, and generate a response.
    """
    st.title("IBM Watson Assistant - DB2 RAG Assistant")

    # Initialize database and load environment variables
    init_db()
    load_dotenv()

    # Retrieve stored credentials or default values
    # api_key = os.getenv("API_KEY")
    # deployment_url = os.getenv("DEPLOYMENT_URL")
    # credentials = get_credentials()
    # if credentials:
    #     api_key, deployment_url = credentials

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
    messages = [{"role": "user", "content": user_question}]
    payload_scoring = {
        "input_data": [
            {
                "fields": ["Search", "access_token"],
                "values": [messages, [get_bearer_token(api_key)]],
            }
        ]
    }

    # Button to generate an email
    if st.button("Query knowledge base"):
        with st.spinner("Sending request to IBM GenAI model..."):
            print ("sending request to:", deployment_url)
            response = requests.post(
                deployment_url,
                json=payload_scoring,
                headers={"Authorization": f"Bearer {get_bearer_token(api_key)}"},
            )
        if response.status_code == 200:
            display_results(response.json())
        else:
            st.error(f"Failed to generate response: {response.text}")

if __name__ == "__main__":
    display_page2()
