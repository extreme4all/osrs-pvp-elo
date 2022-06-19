import logging
import dotenv
import os

dotenv.load_dotenv()

CLIENT_ID = os.environ.get("client_id")
CLIENT_SECRET = os.environ.get("client_secret")