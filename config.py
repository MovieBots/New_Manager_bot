import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_ID = os.environ.get("API_ID", "15646796")
API_HASH = os.environ.get("API_HASH", "08bdb932cf2815a46b2a5f17cf245bfe")
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
PORT = os.environ.get("PORT", "8080")
OWNER_ID = int(os.environ.get("OWNER_ID", "6450266465"))
ADMINS = [int(admin) for admin in os.getenv("ADMINS", "").split()]
