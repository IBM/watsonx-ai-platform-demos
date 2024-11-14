import streamlit as st
import sqlite3
import requests
from dotenv import load_dotenv
import os

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

# Send a scoring request to the IBM GenAI Model
def send_scoring_request(iam_token, deployment_url, client_problem, suggested_resolution):
    response = requests.post(
        deployment_url,
        headers={"Authorization": f"Bearer {iam_token}", "Content-Type": "application/json"},
        json={
            "parameters": {
                "prompt_variables": {
                    "Initial_Client_Problem": client_problem,
                    "My_suggested_Resolution": suggested_resolution
                }
            }
        }
    )
    return response.json().get("results", [{}])[0].get("generated_text", "Error: Response parsing failed.")

# Main function for Page 1 content
def display_page1():
    st.title("Write a nice Email IBM GenAI Model")

    # Initialize database and load stored credentials
    init_db()
    load_dotenv()
    
    api_key = os.getenv("API_KEY")  
    print("default_api_key")
    print(api_key)
    deployment_url = os.getenv("DEPLOYMENT_URL")

    credentials = get_credentials() # Retrieve stored credentials from db if they exist
    if credentials: # if the credentials tuple is not empty use those credentials
        api_key, deployment_url = credentials

    # Input fields for API key and deployment URL
    api_key = st.text_input("Enter your API key", value=api_key, type="password")
    deployment_url = st.text_input("Enter deployment URL", value=deployment_url)


    if st.button("Save API Key and URL") and api_key and deployment_url:
        save_credentials(api_key, deployment_url)
        st.success("Credentials saved!")

    # User input for the problem and suggested resolution
    client_problem = st.text_input("Enter Initial Client Problem", "Describe the client's issue here.")
    suggested_resolution = st.text_input("Enter Suggested Resolution", "Provide a potential solution.")

    if st.button("Generate Email"):
        token = get_ibm_token(api_key)
        if token:
            st.write("Sending request to IBM GenAI model...")
            response_text = send_scoring_request(token, deployment_url, client_problem, suggested_resolution)
            # st.write(f"**Generated Response:**\n\n{response_text}")
            
            # Add CSS for wrapping text in st.code
            st.text_area("Generated Response", response_text, height=800)

        else:
            st.error("Failed to retrieve IBM token. Check your API key.")

if __name__ == "__main__":
    display_page1()