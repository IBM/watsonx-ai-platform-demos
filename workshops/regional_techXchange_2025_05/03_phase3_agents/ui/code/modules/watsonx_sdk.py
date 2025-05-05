import ibm_watsonx_ai
from ibm_watsonx_ai import Credentials
import requests

class WatsonxAI_SDK():
        def __init__(self, 
                    api_key, 
                    space_id : str,
                    deployment_id : str,
                    instance_id: str,
                    version: str,
                    url : str):

            self.space_id = space_id
            self.instance_id = instance_id
            self.deployment_id = deployment_id
            self.url = url
            self.version = version
            self.api_key = api_key

            print(f"***Log url: {self.url}")
            print(f"***Log space_id: {self.space_id}")
            print(f"***Log instance_id: {self.instance_id}")
            print(f"***Log deployment_id: {self.deployment_id}")
            credentials = Credentials(api_key=self.api_key,
                                      url=self.url, 
                                     )
                       
            try:
                self.client = ibm_watsonx_ai.APIClient(credentials, 
                                                       space_id=str(self.space_id),
                                                      )
                #print(f"***Log deployments:\n{self.client.deployments.list()}")
            except Exception as e:
                 print(f"***Log error: {e}")
                 self.client = None
                 
        def getToken (self):
            token_response = requests.post('https://iam.cloud.ibm.com/identity/token', 
                                        data={"apikey": self.api_key, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
            mltoken = token_response.json()["access_token"]
            return mltoken
        
        def convert_messages (self, messages ):
            new_messages = []
            for message in messages:
                entry = {"content": message["content"],
                        "data":{"endog":[0],"exog":[0]},
                        "role": message["role"]}
                new_messages.append(entry)
            return new_messages
        
        def getAgentResponse( self ):
            ai_service_invoke = lambda payload: self.client.deployments.run_ai_service(self.deployment_id, payload)
            return ai_service_invoke
        
        def getAgentStreamResponse( self ):
            ai_service_invoke = lambda payload: self.client.deployments.run_ai_service_stream(self.deployment_id, payload)
            return ai_service_invoke 