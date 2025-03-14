import os
from dotenv import load_dotenv

def watsonx_conf():
    load_dotenv()
    return {
       "WATSONX_APIKEY" : os.getenv('WATSONX_APIKEY'),
       "WATSONX_REGION" : os.getenv('WATSONX_REGION'),
       "WATSONX_DEPLOYMENT_ID" : os.getenv('WATSONX_DEPLOYMENT_ID'),
       "WATSONX_PUB_DEPLOYMENT_URL" : os.getenv('WATSONX_PUB_DEPLOYMENT_URL'),
       "WATSONX_SOFTWARE_NAME" : os.getenv('WATSONX_SOFTWARE_NAME'),
       "WATSONX_SPACE_ID" : os.getenv('WATSONX_SPACE_ID'),
       "WATSONX_URL" : os.getenv('WATSONX_URL'),
       "WATSONX_INSTANCE_ID" : os.getenv('WATSONX_INSTANCE_ID'),
       "WATSONX_VERSION" : os.getenv('WATSONX_VERSION')
    }

def app_conf():
    load_dotenv()
    return {
       "APP_USER" : os.getenv('APP_USER'),
       "APP_PASSWORD" : os.getenv('APP_PASSWORD'),
    }
     
    

