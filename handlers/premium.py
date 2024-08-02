# handlers/premium.py

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta

def buy_premium_command(client: Client, message):
    client.send_message(
        message.chat.id,
        f"Please contact the owner for premium membership: [Owner](tg://user?id={OWNER_ID})",
        parse_mode='markdown'
    )

def callback_query(client: Client, callback_query):
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
        if user_id in premium_users:
            client.send_message(
                user_id,
                "You are already a premium member."
            )
        else:
            plan = data.split("_")[1]
            expiration_date = datetime.now() + timedelta(days={"1m": 30, "3m": 90, "1y": 365}[plan])
            premium_users[user_id] = expiration_date
            client.send_message(user_id,
                f"Membership purchased successfully.\n"
                f"Expiration Date: {expiration_date.strftime('%Y-%m-%d')}"
            )
            client.send_message(
                OWNER_ID,
                f"*Hello My Owner*\n\n"
                f"This person's membership has been updated.\n"
                f"Please take note of it.",
                parse_mode='markdown'
            )
