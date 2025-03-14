import streamlit as st
import json
from modules.load_config import watsonx_conf
from modules.simple_auth import authenticate_user
from modules.watsonx_sdk import WatsonxAI_SDK

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

def response_generator(messages):
    api_key = watsonx_conf()["WATSONX_APIKEY"]
    space_id = str(watsonx_conf()["WATSONX_SPACE_ID"])
    url = str(watsonx_conf()["WATSONX_URL"])
    instance_id = str(watsonx_conf()["WATSONX_INSTANCE_ID"])
    deployment_id = str(watsonx_conf()["WATSONX_DEPLOYMENT_ID"])
    version = str(watsonx_conf()["WATSONX_VERSION"])
    watsonx_ai = WatsonxAI_SDK( api_key, 
                                space_id,
                                deployment_id,
                                instance_id, 
                                version, 
                                url)
    
    ai_service_invoke = watsonx_ai.getAgentResponse()
    messages_payload = {"messages": messages }
    print(f"**Log payload [{messages_payload}]")
    response = ai_service_invoke(messages_payload)
    print(f"**Log response [{response}]")
    resp_choices = response.get("body", response)["choices"]
    choices = resp_choices
    i = 0
    print(f"**Log choices [{i}:{len(choices)}]")
    # Inspect all messages
    for c in choices:
        if 'message' in c: 
            m = c["message"]
            print(f"Message {m}")
            return_message = {}
            tmp_message = {}      
            i = i + 1                         
            if c['message']['role'] == 'assistant':
                if "tool_calls" in c['message']:
                    print(f"**Log tool_calls: {str(c['message']['tool_calls'])}")
                    tmp_message = {"role": c['message']['role'] , "content": str(c['message']['tool_calls'])}
                    
                     # Document tool calls
                    st.text("Role:\n" + tmp_message["role"])
                    st.text("Content:\n" + tmp_message["content"])                                           
                else:
                    content = c['message']['content']
                    role = c['message']['role']
                    return_message = {"role": role , "content": content}

            if c['message']['role'] == 'tool':
                print(f"**Log tool result: {str(c['message']['content'])}")
                tmp_message = {"role": c['message']['role'] , "content": c['message']['content']}
                
                # Document tool result
                st.text("Role: " + tmp_message["role"])
                st.text("Content: " + tmp_message["content"])
        else:
            with st.chat_message("none"):
                 st.markdown(c)

    return return_message['content']


def response_generator_stream (messages):
    api_key = watsonx_conf()["WATSONX_APIKEY"]
    space_id = str(watsonx_conf()["WATSONX_SPACE_ID"])
    url = str(watsonx_conf()["WATSONX_URL"])
    instance_id = str(watsonx_conf()["WATSONX_INSTANCE_ID"])
    deployment_id = str(watsonx_conf()["WATSONX_DEPLOYMENT_ID"])
    version = str(watsonx_conf()["WATSONX_VERSION"])
    watsonx_ai = WatsonxAI_SDK( api_key, 
                                space_id,
                                deployment_id,
                                instance_id, 
                                version, 
                                url)
    
    ai_service_invoke = watsonx_ai.getAgentStreamResponse()
    messages_payload = {"messages": messages }
    response = ai_service_invoke(messages_payload)
    
    full_text = ""
    for r in response:           
            if isinstance(r, str):
                r = json.loads(r)
                print(f"***Log JSON loads: {r}")
                
                i = 0               
                for c in r["choices"]:
                    print(f"***Log messages {c}")
                    return_message = {}
                    tmp_message = {}      
                    i = i + 1  
                    if 'message' in c:                      
                        if c['message']['role'] == 'assistant':
                            
                            if "tool_calls" in c['message']:
                                print(f"**Log tool_calls:\n {str(c['message']['tool_calls'])}")
                                
                                tmp_message = {"role": c['message']['role'] , "content": str(c['message']['tool_calls'])}
                                print(f"**Log return_message 'all':\n {tmp_message}")
                                
                                content_list= tmp_message['content']
                                print(f"**Log return_message content list:\n {content_list}")
                                
                                # Document tool calls
                                st.text("Role:\n" + c['message']['role'])
                                st.text("Content:\n" + tmp_message["content"])                       
                            else:
                                # Build answer
                                delta = c['message']['delta']
                                full_text = full_text + delta
                                print(f"**Log full_text:\n {full_text}")
                                
                                role = c['message']['role']
                                return_message = {"role": role , "content": full_text}

                        if c['message']['role'] == 'tool':
                            print(f"**Log tool result: {str(c['message']['content'])}")
                            tmp_message = {"role": c['message']['role'] , "content": c['message']['content']}
                            
                            st.text("Role:\n" + tmp_message["role"])
                            st.text("Content:\n" + tmp_message["content"])
                    else:
                        with st.chat_message("none"):
                                st.markdown(c)
  
    return return_message['content']
   

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
        st.session_state.messages.append({"role": "system", "data":{"endog":[0],"exog":[0]}, "content": getSystemPrompt()})
    
    # Reset history and reset system prompt
    if reset_button:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "system", "data":{"endog":[0],"exog":[0]}, "content": getSystemPrompt()})

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt:
        
        with st.chat_message("user"):
            st.markdown(prompt)
            # Add user message to chat history
            user_message = {"role": "user", "data":{"endog":[0],"exog":[0]}, "content": prompt}
            st.session_state.messages.append(user_message)
         
        if chat_type == "non-streaming":
            # Display assistant response
            with st.chat_message("assistant"):
                print(f"\n***LOG messages:\n\n{st.session_state.messages}\n\n")
                
                with st.sidebar:
                    st.markdown(f"# Your chat prompt: :sunglasses:\n```text{generate_message_prompt()}```", unsafe_allow_html=False, help=None)
                
                with st.spinner("Wait for full response..."):
                    response = response_generator(st.session_state.messages)
                    st.markdown("Final answer:\n" + response)
                     # Add assistant response to chat history
                    message = {"role": "assistant", "data":{"endog":[0],"exog":[0]}, "content": response}
                    st.session_state.messages.append(message)

        if chat_type == "streaming":
            # Display assistant response
            with st.chat_message("assistant"):
                print(f"\n***LOG messages:\n\n{st.session_state.messages}\n\n")
                
                with st.sidebar:
                    st.markdown(f"# Your chat prompt: :sunglasses:\n```text{generate_message_prompt()}```", unsafe_allow_html=False, help=None)
                
                with st.spinner("Wait for full response..."):
                    response = response_generator_stream(st.session_state.messages)
                    st.markdown("Final answer:\n" + response)
                     # Add assistant response to chat history
                    message = {"role": "assistant", "data":{"endog":[0],"exog":[0]}, "content": response}
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
