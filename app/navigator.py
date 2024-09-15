import streamlit as st
import main
import pneumonia__main

# Set page config
st.set_page_config(
    page_title="Health Prediction App",
    page_icon=":medical_symbol:",
    layout="wide",
    initial_sidebar_state="expanded"
)

def run__main():
    # Check if the user is logged in
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        st.warning('You must be logged in to access this page.')
        st.stop()
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a Prediction App", ["Breast Cancer Prediction", "Pneumonia Classifier"])

    # Run the selected page
    if page == "Breast Cancer Prediction":
        main.main()  # Calls the breast cancer classifier app
    elif page == "Pneumonia Classifier":
        pneumonia__main.main()  # Calls the pneumonia classifier app

if __name__ == '__main__':
    run__main()
