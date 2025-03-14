import sqlite3
import requests
import os
import streamlit as st
from dotenv import load_dotenv

# Initialize the SQLite database for storing API credentials
def init_db():
    """
    Creates a database table to store API key and deployment URLs if it doesn't already exist.
    """
    conn = sqlite3.connect("api_data.db")
    conn.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            api_key TEXT,
            deployment_url_write_email TEXT,
            deployment_url_rag TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Retrieve the latest stored credentials from the database
def get_credentials():
    """
    Fetches the most recently stored API credentials from the database.
    Returns:
        tuple: (api_key, deployment_url_write_email, deployment_url_rag) or None if no credentials exist.
    """
    conn = sqlite3.connect("api_data.db")
    credentials = conn.execute(
        "SELECT api_key, deployment_url_write_email, deployment_url_rag "
        "FROM credentials ORDER BY id DESC LIMIT 1"
    ).fetchone()
    conn.close()
    return credentials if credentials else None

# Save new API credentials to the database
def save_credentials(api_key, deployment_url_write_email, deployment_url_rag):
    """
    Saves new API credentials to the database.
    Args:
        api_key (str): The API key to store.
        deployment_url_write_email (str): Deployment URL for the email assistant.
        deployment_url_rag (str): Deployment URL for RAG.
    """
    conn = sqlite3.connect("api_data.db")
    conn.execute(
        "INSERT INTO credentials (api_key, deployment_url_write_email, deployment_url_rag) "
        "VALUES (?, ?, ?)",
        (api_key, deployment_url_write_email, deployment_url_rag)
    )
    conn.commit()
    conn.close()

# Fetch an IBM Cloud token using the API key
def get_ibm_token(api_key):
    """
    Retrieves an IBM Cloud authentication token.
    Args:
        api_key (str): The IBM Cloud API key.
    Returns:
        str: The access token, or None if the request fails.
    """
    response = requests.post(
        'https://iam.cloud.ibm.com/identity/token',
        data={"apikey": api_key, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
    )
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        return None

# Display configuration settings in the Streamlit UI
def display_configuration(scenario):
    """
    Displays a Streamlit UI for configuring API credentials and deployment URLs.
    Args:
        scenario (str): The use case for the configuration ("write_email" or "rag").
    Returns:
        tuple: (api_key, deployment_url_write_email, deployment_url_rag) from user input or stored credentials.
    """
    # Load environment variables and initialize database
    load_dotenv()
    init_db()

    # Default values from environment variables
    api_key = os.getenv("API_KEY")
    deployment_url_write_email = os.getenv("DEPLOYMENT_URL_WRITE_EMAIL")
    deployment_url_rag = os.getenv("DEPLOYMENT_URL_RAG")

    # Override defaults with the latest stored credentials, if available
    credentials = get_credentials()
    if credentials:
        api_key, deployment_url_write_email, deployment_url_rag = credentials

    # Streamlit configuration interface
    with st.expander("Configuration (API Key and Deployment URL)"):
        st.write("This section is for configuration and usually does not need to be modified.")

        # I know this is ugly, but its necessary to handle multiple pages
        if scenario == "write_email":
            # Input fields for "write_email" configuration
            api_key = st.text_input("Enter your API key", value=api_key or "", type="password")
            deployment_url_write_email = st.text_input("Enter deployment URL for Email Assistant", value=deployment_url_write_email or "")
            if st.button("Save API Key and URL (Email Assistant)") and api_key and deployment_url_write_email:
                save_credentials(api_key, deployment_url_write_email, deployment_url_rag)
                st.success("Credentials for Email Assistant saved successfully!")

        elif scenario == "rag":
            # Input fields for "rag" configuration
            api_key = st.text_input("Enter your API key", value=api_key or "", type="password")
            deployment_url_rag = st.text_input("Enter deployment URL for RAG", value=deployment_url_rag or "")
            if st.button("Save API Key and URL (RAG)") and api_key and deployment_url_rag:
                save_credentials(api_key, deployment_url_write_email, deployment_url_rag)
                st.success("Credentials for RAG saved successfully!")

    return api_key, deployment_url_write_email, deployment_url_rag
