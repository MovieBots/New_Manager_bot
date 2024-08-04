from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def start_command(client: Client, message: Message):
    await client.send_message(
        message.chat.id,
        "Yo what's up\n\nI am a membership provider bot by Arpit.",
        parse_mode='markdown'
    )
    keyboard = [
        [InlineKeyboardButton("Help", callback_data="help"),
         InlineKeyboardButton("Owner", callback_data="owner")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await client.send_message(
        message.chat.id,
        "Here are some commands that only admins and owners can use:",
        reply_markup=reply_markup
    )
