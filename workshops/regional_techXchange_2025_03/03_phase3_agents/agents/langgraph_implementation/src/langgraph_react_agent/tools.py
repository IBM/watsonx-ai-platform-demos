import numpy as np
from typing import List
import requests
import json
import os
from dotenv import load_dotenv

from langchain_core.tools import tool
import logging
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)

@tool(parse_docstring=True)
def db2_expert_service(question: str) -> str:
    """
    The tool 'db2_expert_service' provides all information to answer DB2 seconded level support questions, based on a specific support database.

    Args:
        question: The parameter question contains a technical question related to DB2 usage.

    Returns:
        A string which contains the answer to the given question.
    """
    ################################
    # Functions
    def watsonx_conf():
        load_dotenv()
        return {
        "WATSONX_APIKEY" : os.getenv('WATSONX_APIKEY'),
        "WATSONX_REGION" : os.getenv('WATSONX_REGION'),
        "WATSONX_DEPLOYMENT_ID" : os.getenv('WATSONX_DEPLOYMENT_ID'),
        "WATSONX_DEPLOYMENT_ID_RAG": os.getenv('WATSONX_DEPLOYMENT_ID_RAG'),
        "WATSONX_PUB_DEPLOYMENT_URL" : os.getenv('WATSONX_PUB_DEPLOYMENT_URL'),
        "WATSONX_SOFTWARE_NAME" : os.getenv('WATSONX_SOFTWARE_NAME'),
        "WATSONX_SPACE_ID" : os.getenv('WATSONX_SPACE_ID'),
        "WATSONX_URL" : os.getenv('WATSONX_URL'),
        "WATSONX_INSTANCE_ID" : os.getenv('WATSONX_INSTANCE_ID'),
        "WATSONX_VERSION" : os.getenv('WATSONX_VERSION')
        }

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
    payload_scoring = {
            "messages": [
                    {
                            "content": question,
                            "role": "user"
                    }
            ]
    }
    logging.debug(f"***Log payload 'db2_documentation':\n{payload_scoring}")

    response_scoring = requests.post(
        f"https://{watsonx_conf()['WATSONX_REGION']}.ml.cloud.ibm.com/ml/v4/deployments/{watsonx_conf()['WATSONX_DEPLOYMENT_ID_RAG']}/ai_service?version=2021-05-01",
        json=payload_scoring,
        headers={"Authorization": "Bearer " + get_bearer_token()}, 
    )

    logging.debug(f"***Log response 'db2_documentation':\n{response_scoring.json()['choices']}")

    result_text = response_scoring.json()['choices'][0]['message']['content']

    return result_text

@tool(parse_docstring=True)
def email_expert_service(question: str, answer: str) -> str:
    """
    The 'email_expert_service' tool generates a well-phrased and polite email response based on the provided issue resolution. The email should acknowledge the user's concern, explain the resolution clearly, and offer further assistance if needed. Keep the tone professional, friendly, and concise.

    Args:
       question: The parameter question contains a technical question related to DB2 usage.
       answer: Contains the answer to given the question.

    Returns:
        Full content of generated email text.
    """
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
    payload_scoring = {
        "parameters": {
                "prompt_variables": {
                        "Initial_Client_Problem": question,
                        "My_suggested_Resolution": answer,
                        "Your_name": "Tom Bot"
                }
        }
    }
    logging.debug(f"***Log payload 'email_expert_service':\n{payload_scoring}")

    token = f"Bearer  {get_bearer_token()}"
    header = {"Content-Type": "application/json", "Authorization": token }
    response_scoring = requests.post(
        f"https://{watsonx_conf()['WATSONX_REGION']}.ml.cloud.ibm.com/ml/v1/deployments/{watsonx_conf()['WATSONX_DEPLOYMENT_ID_EMAIL']}/text/generation?version=2021-05-01",
        data= json.dumps(payload_scoring), 
        verify= False,
        headers= header, 
    )

    logging.debug(f"***Log response all 'email_expert_service':\n{response_scoring.json()['results']}")
    
    result_text = response_scoring.json()['results'][0]['generated_text']

    logging.debug(f"***Log response text 'email_expert_service':\n{result_text}")

    return result_text
