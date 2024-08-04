import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_ID = os.environ.get("API_ID", "29236719")
API_HASH = os.environ.get("API_HASH", "1ccf1bd0a86af974e3210a55f662c062")
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
PORT = os.environ.get("PORT", "8080")
OWNER_ID = int(os.environ.get("OWNER_ID", "893383574"))
ADMINS = [int(admin) for admin in os.getenv("ADMINS", "893383574").split()]

if not API_ID or not API_HASH or not TG_BOT_TOKEN:
    raise ValueError("Missing API_ID, API_HASH, or TG_BOT_TOKEN in environment variables.")
