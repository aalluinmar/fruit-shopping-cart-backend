import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Base configuration class.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
