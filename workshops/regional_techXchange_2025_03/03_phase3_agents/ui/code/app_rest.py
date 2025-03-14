import streamlit as st
import time
from modules.load_config import watsonx_conf
from modules.simple_auth import authenticate_user
from regional_techxchange_repo_2025.agents_dev_langgraph.ui.code.modules.watsonx_rest import WatsonxAI_REST

###################
# Variables
system_prompt = """
## System Instructions
You are a knowledgeable and friendly AI assistant named Thomas. 
Your role is to help users by answering their questions, providing information, and offering guidance to the best of your abilities. When responding, use a warm and professional tone and break down complex topics into easy-to-understand explanations. If you are unsure about an answer, it's okay to say you don't know rather than guessing. 
Execute a tool call whenever you see fit.
"""

###################
# Functions

def response_generator( messages):
    apikey = watsonx_conf()["WATSONX_APIKEY"]
    region = watsonx_conf()["WATSONX_REGION"]
    deployment_id = watsonx_conf()["WATSONX_DEPLOYMENT_ID"]
    pub_deployment_url = watsonx_conf()["WATSONX_PUB_DEPLOYMENT_URL"]
    watsonx_ai = WatsonxAI_REST( apikey, region, deployment_id, pub_deployment_url)
    
    response = watsonx_ai.getAgentResponse(messages)
    return response

def generate_message_prompt ():
    result_prompt = "" 
    for m in st.session_state.messages:
        result_prompt = result_prompt + '\n' + f'"role": {m["role"]}, "content": {m["content"]}'
    return result_prompt

def chat_type_select_box():
     
     label = "Select how you want to interact with the model in the Chat."
     options = ['non-streaming']
     chat_type = st.selectbox(label, options, index=0, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
     return chat_type 

def setSystemPrompt ( in_system_prompt):
     system_prompt = in_system_prompt

def getSystemPrompt ( ):   
     return system_prompt

def execution():

    # Init configuration
    chat_type = chat_type_select_box()
    reset_button= st.button("Reset Chat", icon="🔄", type="primary")
    user_message = {}
    prompt = st.chat_input("Say something")

    # Initialize chat history and set system prompt
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "system", "content": getSystemPrompt()})
    
    # Reset history and reset system prompt
    if reset_button:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "system", "content": getSystemPrompt()})

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt:
        
        with st.chat_message("user"):
            st.markdown(prompt)
            # Add user message to chat history
            user_message = {"role": "user", "content": prompt}
            st.session_state.messages.append(user_message)
         
        if chat_type == "non-streaming":
            # Display assistant response
            with st.chat_message("assistant"):
                print(f"\n***LOG messages:\n\n{st.session_state.messages}\n\n")
                
                with st.sidebar:
                    st.markdown(f"# Your chat prompt: :sunglasses:\n```text{generate_message_prompt()}```", unsafe_allow_html=False, help=None)
                
                with st.spinner("Wait for full response..."):
                    response = response_generator(st.session_state.messages)
                    st.markdown(response)
                     # Add assistant response to chat history
                    message = {"role": "assistant", "content": response}
                    st.session_state.messages.append(message) 

###################
# Execution
st.set_page_config(page_title="Simple Chat with watsonx.ai LangGraph Agent REST AOI", layout="wide")
logo_url = './app_imgs/chat_image.png'
st.sidebar.image(logo_url)

st.markdown("""
        <style>
            .reportview-container {
                margin-top: -2em;
            }
            #MainMenu {visibility: hidden;}
            .stDeployButton {display:none;}
            footer {visibility: hidden;}
            #stDecoration {display:none;}
        </style>
    """, unsafe_allow_html=True)

if authenticate_user():
    execution()



      
