import os

API_ID = os.environ.get("API_ID", "your_api_id")
API_HASH = os.environ.get("API_HASH", "your_api_hash")
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "your_bot_token")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
PORT = os.environ.get("PORT", "8080")
OWNER_ID = int(os.environ.get("OWNER_ID", "6450266465"))
