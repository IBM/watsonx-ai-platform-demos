from modules.load_config import app_conf
import streamlit as st


def creds_entered():

    if ((st.session_state["user"].strip() == app_conf()['APP_USER']) and
        (st.session_state["passwd"].strip() == app_conf()['APP_PASSWORD'])
       ):
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("Please enter a password.")
        elif not st.session_state["user"]:
            st.warning("Please enter your user name.")
        else:
            st.error("Invalid Username/Password :face_with_raised_eyebrow:")    
    
    return
    
def authenticate_user():

    ###
    # This function first checks if the session state contains an authenticated variable. 
    # If not, it creates text input fields for the user to enter their username and password. 
    # The on_change parameter is set to the creds_entered() function, so that whenever the user types into the fields, the creds_entered() function is called.
    # If the session state does contain an authenticated variable, the function checks its value. 
    # If it's True, the function returns True, indicating that the user is authenticated. Otherwise, it creates text input fields for the user to enter their username and password again (in case they entered them incorrectly), and then returns False.
    ###
    
    if "authenticated" not in st.session_state:
        st.text_input(label="Username :", value="", key="user", on_change=creds_entered)
        st.text_input(label="Password :", value="", key="passwd", on_change=creds_entered)
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="Username :", value="", key="user", on_change=creds_entered)
            st.text_input(label="Password :", value="", key="passwd", on_change=creds_entered)
            return False