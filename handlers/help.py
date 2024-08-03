from pyrogram import Client, filters
from pyrogram.types import Message

async def help_command(client: Client, message: Message):
    await message.reply("Here is how to use me:\nUse /buy_premium to buy membership.\nIf you want to know more, contact Owner.")

