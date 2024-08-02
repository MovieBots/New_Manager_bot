from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
import os
import time
from database.database import add_premium_user, remove_premium_user, get_premium_users

# Configuration (move to config.py later)
API_KEY = "your_api_key"
OWNER_ID = 123456789
ADMIN_IDS = {123456789}  # Set of admin IDs
API_ID = "your_api_id"
API_HASH = "your_api_hash"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=API_KEY)

@app.on_message(filters.command("start"))
def start_command(client, message):
    client.send_message(
        message.chat.id,
        "Yo what's up\n\nI am a membership provider bot.",
        parse_mode='markdown'
    )
    keyboard = [
        [InlineKeyboardButton("Help", callback_data="help"),
         InlineKeyboardButton("Owner", callback_data="owner")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    client.send_message(
        message.chat.id,
        "Here are some commands that only admins and owners can use:",
        reply_markup=reply_markup
    )

@app.on_message(filters.command("buy_premium"))
def buy_premium_command(client, message):
    client.send_message(
        message.chat.id,
        f"Please contact the owner for premium membership: [Owner](tg://user?id={OWNER_ID})",
        parse_mode='markdown'
    )

@app.on_callback_query()
def callback_query(client, callback_query):
    user_id = callback_query.from_user.id
    data = callback_query.data

    if data == "buy_premium":
        keyboard = [
            [InlineKeyboardButton("99 rs for 1 month", callback_data="premium_1m"),
             InlineKeyboardButton("250 rs for 3 months", callback_data="premium_3m"),
             InlineKeyboardButton("500 rs for 1 year", callback_data="premium_1y")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        client.send_message(
            callback_query.message.chat.id,
            "Select a membership plan:",
            reply_markup=reply_markup
        )

    elif data.startswith("premium"):
        plan = data.split("_")[1]
        if plan == "1m":
            expiration_date = datetime.now() + timedelta(days=30)
        elif plan == "3m":
            expiration_date = datetime.now() + timedelta(days=90)
        elif plan == "1y":
            expiration_date = datetime.now() + timedelta(days=365)

        add_premium_user(user_id, expiration_date)
        client.send_message(user_id,
            f"Membership purchased successfully.\n"
            f"Expiration Date: {expiration_date.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        client.send_message(
            OWNER_ID,
            f"Hello My Owner\n\nThis person's membership has been updated: [user](tg://user?id={user_id}). Please take note of it.",
            parse_mode='markdown'
        )

@app.on_message(filters.command(["add_user", "remove_user", "stats"]) & (filters.user(OWNER_ID) | filters.user(ADMIN_IDS)))
def handle_admin_commands(client, message):
    command = message.text.split()[0].strip().lower()
    user_id = int(message.text.split()[1])

    if command == "/add_user":
        keyboard = [
            [InlineKeyboardButton("2 minutes", callback_data=f"add_premium_2m_{user_id}"),
             InlineKeyboardButton("5 hours", callback_data=f"add_premium_5h_{user_id}"),
             InlineKeyboardButton("1 month", callback_data=f"add_premium_1m_{user_id}"),
             InlineKeyboardButton("3 months", callback_data=f"add_premium_3m_{user_id}"),
             InlineKeyboardButton("1 year", callback_data=f"add_premium_1y_{user_id}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        client.send_message(
            message.chat.id,
            "Select the duration for the premium membership:",
            reply_markup=reply_markup
        )

    elif command == "/remove_user":
        remove_premium_user(user_id)
        client.send_message(
            message.chat.id,
            f"User {user_id} has been removed from premium membership."
        )

    elif command == "/stats":
        users = get_premium_users()
        keyboard = [
            [InlineKeyboardButton(f"User {user_id}", callback_data=f"user_details_{user_id}")]
            for user_id, _ in users
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        client.send_message(
            message.chat.id,
            "Premium Users:",
            reply_markup=reply_markup
        )

@app.on_callback_query(filters.regex(r"user_details_(\d+)"))
def user_details_callback(client, callback_query):
    user_id = int(callback_query.data.split("_")[2])
    user = app.get_users(user_id)
    details = (f"Name: {user.first_name} {user.last_name or ''}\n"
               f"Username: @{user.username or 'N/A'}\n"
               f"ID: {user.id}\n"
               f"Expiration Date: {premium_users.get(user_id, 'N/A')}")
    client.send_message(callback_query.message.chat.id, details)

@app.on_callback_query()
def handle_premium_duration(client, callback_query):
    data = callback_query.data
    if data.startswith("add_premium"):
        _, plan, user_id = data.split("_")
        user_id = int(user_id)
        if plan == "2m":
            expiration_date = datetime.now() + timedelta(minutes=2)
        elif plan == "5h":
            expiration_date = datetime.now() + timedelta(hours=5)
        elif plan == "1m":
            expiration_date = datetime.now() + timedelta(days=30)
        elif plan == "3m":
            expiration_date = datetime.now() + timedelta(days=90)
        elif plan == "1y":
            expiration_date = datetime.now() + timedelta(days=365)

        add_premium_user(user_id, expiration_date)
        client.send_message(user_id,
            f"Membership added successfully.\n"
            f"Expiration Date: {expiration_date.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        client.send_message(
            OWNER_ID,
            f"Hello My Owner\n\nThis person's membership has been updated: [user](tg://user?id={user_id}). Please take note of it.",
            parse_mode='markdown'
        )

@app.on_stop
def save_on_stop():
    save_admins()

if __name__ == "__main__":
    app.run()
    while True:
        check_membership_expiration()
        time.sleep(3600)
