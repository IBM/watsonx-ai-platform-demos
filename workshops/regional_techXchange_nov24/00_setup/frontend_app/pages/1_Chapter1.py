import os
import requests
import streamlit as st
from dotenv import load_dotenv
from utils.utils import init_db, get_credentials, save_credentials, get_ibm_token, display_configuration


def send_scoring_request(iam_token, deployment_url, client_problem, suggested_resolution, your_name):
    """
    Send a scoring request to the IBM GenAI Model to generate an email.

    Args:
        iam_token (str): IBM IAM token for authentication.
        deployment_url (str): Deployment URL of the GenAI model.
        client_problem (str): Description of the client's issue.
        suggested_resolution (str): Proposed resolution to the issue.
        your_name (str): Name of the user generating the email.

    Returns:
        str: The generated email text or an error message.
    """
    response = requests.post(
        deployment_url,
        headers={"Authorization": f"Bearer {iam_token}", "Content-Type": "application/json"},
        json={
            "parameters": {
                "prompt_variables": {
                    "Initial_Client_Problem": client_problem,
                    "My_suggested_Resolution": suggested_resolution,
                    "My_name": your_name
                }
            }
        }
    )
    if response.status_code == 200:
        return response.json().get("results", [{}])[0].get("generated_text", "Error: Response parsing failed.")
    else:
        return f"Error: Failed to retrieve response. Status code: {response.status_code}"


def display_page1():
    """
    Main function to render the Streamlit app for generating client-facing emails using IBM GenAI.
    """
    st.title("Generate a Professional Email with IBM GenAI")

    # Initialize database and load environment variables
    init_db()
    load_dotenv()

    # Get API key and deployment URL from configuration section
    api_key, deployment_url_rag, deployment_url_write_email = display_configuration()
    deployment_url = deployment_url_write_email

    default_name = "Maximilian Jesch"
    default_problem = ("We created a new index on the products table to improve searches,"
                       "but now the CHECK_STOCK routine is significantly slower.")
    default_resolution = ("Review the new index's impact on the routine's queries and "
                          "consider adjusting query structure or index strategy.")

    # Input fields for the email generation process
    your_name = st.text_input("Enter Your Name", value=default_name)
    client_problem = st.text_area("Enter Initial Client Problem", value=default_problem, height=150)
    suggested_resolution = st.text_area("Enter Suggested Resolution", value=default_resolution, height=150)

    # Generate email when the button is clicked
    if st.button("Generate Email"):
        token = get_ibm_token(api_key)
        if token:
            with st.spinner("Sending request to IBM GenAI model..."):
                response_text = send_scoring_request(token, deployment_url, client_problem, suggested_resolution, your_name)
            st.text_area("Generated Response", response_text, height=400)
        else:
            st.error("Failed to retrieve IBM token. Check your API key.")


if __name__ == "__main__":
    display_page1()
