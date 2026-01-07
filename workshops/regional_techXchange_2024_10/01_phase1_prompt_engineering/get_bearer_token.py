import requests
import os

# Get API key from environment variable
api_key = os.environ.get("IBM_CLOUD_API_KEY", "YOUR_API_KEY_HERE")

# Function to get the bearer token
def get_bearer_token(api_key):
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
    
print(get_bearer_token(api_key)) 