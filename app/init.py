import streamlit as st
import requests
import json
import logging
from firebase_setup import initialize_firebase
import navigator  # Import navigator.py to navigate after login

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO to capture INFO level messages and above

# Initialize Firebase
initialize_firebase()

# Firebase Auth REST API URL
FIREBASE_AUTH_URL = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyAoFaX8cBgghqvz9tt7xlGo0q7EsyFdY1g'

def app():
    # Check if user is already logged in and show navigator if true
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        navigator.run__main()  # Call the navigator.py app directly
        return  # Stop further execution of the login page

    st.title('Welcome To Login')

    choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])

    def handle_login(email, password):
        try:
            response = requests.post(
                FIREBASE_AUTH_URL,
                headers={'Content-Type': 'application/json'},
                data=json.dumps({
                    'email': email,
                    'password': password,
                    'returnSecureToken': True
                })
            )
            response_data = response.json()
            if 'idToken' in response_data:
                # Store login state
                st.session_state['logged_in'] = True
                st.session_state['email'] = email

                success_message = f'Login successful for user: {email}'
                logging.info(success_message)  # Log the success message
                
                # Redirect to the navigator page
                st.experimental_rerun()  # Refresh to apply the logged_in state and reroute to navigator

            else:
                error_message = 'Login Failed: ' + response_data.get('error', {}).get('message', 'Unknown error')
                st.warning(error_message)
                logging.warning(error_message)  # Log the warning message
        except Exception as e:
            error_message = f'Error during login: {e}'
            st.warning(error_message)
            logging.error(error_message)  # Log the error message

    if choice == 'Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if st.button('Login'):
            handle_login(email, password)

    else:  # Sign Up
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter Username')

        if st.button('Create account'):
            try:
                response = requests.post(
                    'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyAoFaX8cBgghqvz9tt7xlGo0q7EsyFdY1g',
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps({
                        'email': email,
                        'password': password,
                        'returnSecureToken': True
                    })
                )
                response_data = response.json()
                if 'idToken' in response_data:
                    st.success('Account created successfully!')
                    st.markdown('Login')
                    st.balloons()
                else:
                    error_message = 'Error creating account: ' + response_data.get('error', {}).get('message', 'Unknown error')
                    st.error(error_message)
                    logging.error(error_message)  # Log the error message
            except Exception as e:
                error_message = f'Error creating account: {e}'
                st.error(error_message)
                logging.error(error_message)  # Log the error message

if __name__ == '__main__':
    app()
