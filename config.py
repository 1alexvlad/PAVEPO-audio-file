import os
from dotenv import load_dotenv
from pydantic import BaseConfig

load_dotenv()

class Config(BaseConfig):
    CLIENT_ID: str = os.environ.get("clientID")
    CLIENT_SECRET: str = os.environ.get("client_secret")
    REDIRECT_URL: str = os.environ.get("redirect_url")
    AUTHORIZE_URL: str = os.environ.get("authorize_url") 
    TOKEN_URL: str = os.environ.get("token_url")

config = Config()
