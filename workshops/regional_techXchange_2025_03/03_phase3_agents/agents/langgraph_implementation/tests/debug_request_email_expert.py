import requests
import os
import json
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

token = f"Bearer  {get_bearer_token()}"
header = {"Content-Type": "application/json", "Authorization": token }

payload_scoring = { "parameters": { "prompt_variables" : {
                                                            "Initial_Client_Problem" : "A routine that usually runs in under 2 minutes is now timing out after 30 minutes. No changes were made to the routine or database. How do I resolve this?",
                                                            "My_suggested_Resolution" : "Investigate potential database locking or blocking issues. Advise checking for long-running transactions or locks using db2pd -locks or reviewing system performance metrics.",
                                                            "Your_name": "Tom Bot"
                                                         }
                                  }
                  }

print(f"***Log payload:\n{payload_scoring}")
print(f"***Log url:\nhttps://{watsonx_conf()['WATSONX_REGION']}.ml.cloud.ibm.com/ml/v1/deployments/{watsonx_conf()['WATSONX_DEPLOYMENT_ID_EMAIL']}/text/generation?version=2021-05-01\n")

#https://us-south.ml.cloud.ibm.com/ml/v1/deployments/7b2b638f-01d1-43c1-aba0-a683b3a2a73e/text/generation?version=2021-05-01
response_scoring = requests.post(
    f"https://{watsonx_conf()['WATSONX_REGION']}.ml.cloud.ibm.com/ml/v1/deployments/{watsonx_conf()['WATSONX_DEPLOYMENT_ID_EMAIL']}/text/generation?version=2021-05-01",
    data= json.dumps(payload_scoring), 
    verify= False,
    headers= header, 
)

print(f"***Log response:\n{response_scoring.status_code}\n{response_scoring.text}")
