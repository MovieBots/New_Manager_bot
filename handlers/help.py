# handlers/help.py

from pyrogram import Client, filters

def help_command(client: Client, message):
    client.send_message(
        message.chat.id,
        "Here is how to use me:\n"
        "Use /buy_premium to buy membership.\n"
        "If you want to know more, contact Owner."
    )
