import sqlite3
import requests
import os
import streamlit as st
from dotenv import load_dotenv

# Initialize database connection for storing API key and deployment URL
def init_db():
    conn = sqlite3.connect("api_data.db")
    conn.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            api_key TEXT,
            deployment_url TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Retrieve the latest stored credentials from the database
def get_credentials():
    conn = sqlite3.connect("api_data.db")
    credentials = conn.execute("SELECT api_key, deployment_url FROM credentials ORDER BY id DESC LIMIT 1").fetchone()
    conn.close()
    return credentials if credentials else None

# Save new credentials to the database
def save_credentials(api_key, deployment_url):
    conn = sqlite3.connect("api_data.db")
    conn.execute("INSERT INTO credentials (api_key, deployment_url) VALUES (?, ?)", (api_key, deployment_url))
    conn.commit()
    conn.close()
    
# Retrieve IBM Cloud token
def get_ibm_token(api_key):
    response = requests.post(
        'https://iam.cloud.ibm.com/identity/token',
        data={"apikey": api_key, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
    )
    return response.json().get("access_token") if response.status_code == 200 else None

def display_configuration():
    """
    Display the configuration section for API Key and Deployment URL.

    Returns:
        tuple: (api_key, deployment_url) from user input or stored credentials.
    """
    # Initialize database and load environment variables
    load_dotenv()
    api_key = os.getenv("API_KEY")
    deployment_url_rag = os.getenv("DEPLOYMENT_URL_RAG")
    deployment_url_write_email = os.getenv("DEPLOYMENT_URL_WRITE_EMAIL")

    credentials = get_credentials()
    if credentials:
        api_key, deployment_url = credentials

    # Separate API Key and URL section in a collapsible container
    with st.expander("Configuration (API Key and Deployment URL)"):
        st.write("This section is for configuration and usually does not need to be modified.")
        api_key = st.text_input("Enter your API key", value=api_key or "", type="password")
        deployment_url = st.text_input("Enter deployment URL", value=deployment_url or "")

        # Save credentials when the button is clicked
        if st.button("Save API Key and URL") and api_key and deployment_url:
            save_credentials(api_key, deployment_url)
            st.success("Credentials saved!")

    return api_key, deployment_url_rag, deployment_url_write_email