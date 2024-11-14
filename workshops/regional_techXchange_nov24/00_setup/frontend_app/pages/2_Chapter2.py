import streamlit as st
import requests

#TODOS: 
# 1. get credentials 
# 2. field for question --> send request

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

def display_page2():
    st.title("Page 2")
    default_question= "I'm trying to execute a routine named GET_CUSTOMER_DATA in DB2, but it returns an error: 'Routine not found in schema.' I double-checked the routine name, and it exists in the catalog."
    user_question = st.text_input("Enter your question", value=default_question)
    
    ### change this! ###
    api_key = "0-yL63WB4sv1_lB-rx3vdvXfnYh5MrDT7vXTOqqxkBX4"  # SENSITIVE!! DO NOT SHARE OR UPLOAD TO GITHUB

    
    # header = {"Content-Type": "application/json", "Authorization": "Bearer " 
    #           + get_bearer_token(api_key)}

    messages = []
    messages.append({ "role" : "user", "content": user_question })
    payload_scoring = {
        "input_data": [
            {
                "fields": ["Search", "access_token"],
                "values": [messages, [get_bearer_token(api_key)] #this is kind of redundant, but it's the way the retriever gets the token to send a request to watsonx.ai
                ],
            }
        ]
    }

    if st.button("Generate Email"):
        response_scoring = requests.post(
            "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/9aa835da-e675-437b-be80-2b905f99fe50/predictions?version=2021-05-01",
            json=payload_scoring,
            headers={"Authorization": "Bearer " + get_bearer_token(api_key)}, 
        )
        print(response_scoring.json())
        st.text_area("Generated Response", response_scoring.json(), height=800)
        
if __name__ == "__main__":
    display_page2()
