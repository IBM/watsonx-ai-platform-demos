import requests

class WatsonxAI_REST():
    
    def __init__(self, 
                 apikey, 
                 region, 
                 deployment_id,
                 pub_deployment_url):

        self.deployment_id = deployment_id
        self.pub_deployment_url = pub_deployment_url
        self.region = region
        self.api_key = apikey

    def getToken (self):
        #print(f"***Log API KEY: {self.api_key}")
        token_response = requests.post('https://iam.cloud.ibm.com/identity/token', 
                                       data={"apikey": self.api_key, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
        #print(f"***Log RAW TOKEN: {token_response.raw}")
        mltoken = token_response.json()["access_token"]
        #print(f"***Log TOKEN: {mltoken}")
        return mltoken

    def convert_messages (self, messages ):
        new_messages = []
        for message in messages:
            entry = {"content": message["content"],
                     "data":{"endog":[0],"exog":[0]},
                     "role": message["role"]}
            new_messages.append(entry)
        return new_messages


    def getAgentResponse( self, messages ):
        print(f"***Log messages: {messages}")
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + self.getToken()}
        
        # Use message histroy
        payload_scoring = {"messages": self.convert_messages(messages)}
        
        deployment_url = f"{self.pub_deployment_url}/{self.deployment_id}/ai_service?version=2021-05-01"
        print(f"***Log url: {deployment_url}")
        try:
            deployment_url = 'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5a8f9036-9fe8-4bae-8cc8-02baaa5f69e6/ai_service?version=2021-05-01'
            response_scoring = requests.post( deployment_url, 
                                              json=payload_scoring,
                                              headers= headers )
            print("Scoring response")
            print(response_scoring.json())

            # extract the result
            choices = response_scoring.json()['choices']
            print(f"**Log choices: {choices}")
            return_message = {}
            i = 0

            # Inspect all messages
            for message in choices:
                i = i + 1
                print(f"**Log choices [{i}:{len(choices)}]")              
                if message['message']['role'] == 'assistant':
                     
                     if "tool_calls" in message['message']:
                        print(f"**Log tool_calls: {str(message['message']['tool_calls'])}")
                        return_message = {"role": message['message']['role'] , "content": str(message['message']['tool_calls'])}                           
                     else:
                         content = message['message']['content']
                         role = message['message']['role']
                         return_message = {"role": role , "content": content}

                if message['message']['role'] == 'tool':

                    print(f"**Log tool result: {str(message['message']['content'])}")
                    return_message = {"role": message['message']['role'] , "content": message['message']['content']}

            return return_message['content']
        
        except Exception as error:
            
            print(f"***Log: Error: {error}")
            return {"error": {error}}

            

        
        

