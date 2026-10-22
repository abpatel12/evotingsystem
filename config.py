import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("APP_SECRET_KEY", "development-only-change-this")
    VOTE_HMAC_KEY = os.getenv("VOTE_HMAC_KEY", "")
    DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"
    MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "electronic_voting_db")
    TOKEN_TTL_MINUTES = int(os.getenv("TOKEN_TTL_MINUTES", "10"))
