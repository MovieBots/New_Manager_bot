from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
from database import database  # Import the database module

premium_users = {}  # You may need to initialize this or import it from your main script

def handle_admin_commands(client: Client, message):
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
        if user_id in premium_users:
            del premium_users[user_id]
            client.send_message(
                message.chat.id,
                f"User {user_id} has been removed from premium membership."
            )
        else:
            client.send_message(
                message.chat.id,
                f"User {user_id} is not a premium member."
            )

    elif command == "/stats":
        keyboard = [
            [InlineKeyboardButton(f"User {user_id}", callback_data=f"user_details_{user_id}")]
            for user_id in premium_users.keys()
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        client.send_message(
            message.chat.id,
            "Premium Users:",
            reply_markup=reply_markup
        )

