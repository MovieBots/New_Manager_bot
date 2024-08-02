# bot.py

from pyrogram import Client
from config import API_ID, API_HASH, API_KEY, OWNER_ID, ADMIN_IDS
from database.database import load_admin_ids, save_admin_ids
from handlers import start, help, premium, admin, user_stats
import time
from datetime import datetime, timedelta

# Convert ADMIN_IDS string to a set of integers
admin_ids = load_admin_ids()
admin_ids.update(map(int, ADMIN_IDS.split(',')))

# Initialize Pyrogram Client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=API_KEY)

# Dictionary to store premium users and their expiration times
premium_users = {}

@app.on_message(filters.command("start"))
def start_command(client, message):
    start.start_command(client, message)

@app.on_message(filters.command("help"))
def help_command(client, message):
    help.help_command(client, message)

@app.on_message(filters.command("buy_premium"))
def buy_premium_command(client, message):
    premium.buy_premium_command(client, message)

@app.on_message(filters.command(["add_user", "remove_user", "stats"]) & (filters.user(OWNER_ID) | filters.user(admin_ids)))
def handle_admin_commands(client, message):
    admin.handle_admin_commands(client, message)

@app.on_callback_query()
def callback_query(client, callback_query):
    data = callback_query.data
    if data.startswith("user_details"):
        user_stats.user_details_callback(client, callback_query)
    else:
        premium.callback_query(client, callback_query)

# Function to handle membership expiration check
def check_membership_expiration():
    now = datetime.now()
    for user_id, expiration_date in list(premium_users.items()):
        if now > expiration_date:
            del premium_users[user_id]
            app.send_message(
                user_id,
                "Yo dude\n\n"
                "Your membership is over. Contact admin for more details."
            )
            app.send_message(
                OWNER_ID,
                f"Hello My Owner\n\n"
                f"This person's membership is over: [user](tg://user?id={user_id}). Please remove them."
            )

# Save admin IDs when app stops
@app.on_stop
def save_on_stop():
    save_admin_ids(admin_ids)

# Run the bot
if __name__ == "__main__":
    app.run()

    # Periodically check for membership expiration
    while True:
        check_membership_expiration()
        time.sleep(3600)  # Check every hour

