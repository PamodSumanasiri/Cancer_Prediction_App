import firebase_admin
import logging
from firebase_admin import credentials

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO to capture INFO level messages and above

def initialize_firebase():
    try:
        # Check if Firebase app is already initialized
        if not firebase_admin._apps:
            cred = credentials.Certificate('app/machinelearning-cfde7-38e760989a07.json')
            firebase_admin.initialize_app(cred)
            logging.info('Firebase initialized successfully.')
        else:
            logging.info('Firebase is already initialized.')
    except Exception as e:
        logging.error(f'Error initializing Firebase: {e}')
