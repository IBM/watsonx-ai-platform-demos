import requests
import os
from dotenv import load_dotenv

################################
# Functions
def watsonx_conf():
    load_dotenv()
    return {
       "WATSONX_APIKEY" : os.getenv('WATSONX_APIKEY'),
       "WATSONX_REGION" : os.getenv('WATSONX_REGION'),
       "WATSONX_DEPLOYMENT_ID" : os.getenv('WATSONX_DEPLOYMENT_ID'),
       "WATSONX_DEPLOYMENT_ID_RAG": os.getenv('WATSONX_DEPLOYMENT_ID_RAG'),
       "WATSONX_DEPLOYMENT_ID_EMAIL": os.getenv('WATSONX_DEPLOYMENT_ID_EMAIL'),
       "WATSONX_PUB_DEPLOYMENT_URL" : os.getenv('WATSONX_PUB_DEPLOYMENT_URL'),
       "WATSONX_SOFTWARE_NAME" : os.getenv('WATSONX_SOFTWARE_NAME'),
       "WATSONX_SPACE_ID" : os.getenv('WATSONX_SPACE_ID'),
       "WATSONX_URL" : os.getenv('WATSONX_URL'),
       "WATSONX_INSTANCE_ID" : os.getenv('WATSONX_INSTANCE_ID'),
       "WATSONX_VERSION" : os.getenv('WATSONX_VERSION')
    }

# Function to get the bearer token
def get_bearer_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": watsonx_conf()["WATSONX_APIKEY"]
    }
    response = requests.post(url, headers=headers, data=data, verify=False)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Failed to retrieve token: {response.text}")
        return None

################################
# Execution

header = {"Content-Type": "application/json", "Authorization": "Bearer " + get_bearer_token()}

messages = []
remote_question = "What is a DB2 routine?" # CHANGE THIS TO THE QUESTION YOU WANT TO ASK
messages.append({ "role" : "user", "content": remote_question })
payload_scoring = {
        "messages": [
                {
                        "content": "What is a DB2 routine?",
                        "role": "user"
                }
        ]
}

print(f"***Log payload:\n{payload_scoring}")

response_scoring = requests.post(
    f"https://{watsonx_conf()['WATSONX_REGION']}.ml.cloud.ibm.com/ml/v4/deployments/{watsonx_conf()['WATSONX_DEPLOYMENT_ID']}/ai_service?version=2021-05-01",
    json=payload_scoring,
    headers={"Authorization": "Bearer " + get_bearer_token()}, 
)

print(f"***Log response:\n{response_scoring.json()}")
