import logging
import os
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_BOT_WORKERS = int(os.getenv("TG_BOT_WORKERS", "4"))
OWNER_ID = int(os.getenv("OWNER_ID"))
ADMINS = [int(admin) for admin in os.getenv("ADMINS", "").split()]

class Bot(Client):
    def __init__(self):
        super().__init__(
            "my_bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TG_BOT_TOKEN,
            workers=TG_BOT_WORKERS,
        )
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    async def start(self):
        await super().start()
        self.logger.info("Bot started.")
        self.logger.info("""
 █████╗ ███╗   ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗
██╔══██╗████╗  ██║██║██╔════╝██║  ██║██║████╗  ██║
███████║██╔██╗ ██║██║███████╗███████║██║██╔██╗ ██║
██╔══██║██║╚██╗██║██║╚════██║██╔══██║██║██║╚██╗██║
██║  ██║██║ ╚████║██║███████║██║  ██║██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ 
""")

    async def stop(self, *args):
        await super().stop()
        self.logger.info("Bot stopped.")

    def run(self):
        super().run()
        self.start()
        self.idle()

bot = Bot()

# Import handlers
from handlers.start import start_command
from handlers.help import help_command
from handlers.premium import buy_premium_command, callback_query
from handlers.admin import handle_admin_commands
from handlers.user_stats import user_details_callback

# Add handlers
bot.add_handler(MessageHandler(start_command, filters.command("start") & filters.private))
bot.add_handler(MessageHandler(help_command, filters.command("help") & filters.private))
bot.add_handler(MessageHandler(buy_premium_command, filters.command("buy_premium") & filters.private))
bot.add_handler(MessageHandler(handle_admin_commands, filters.user(ADMINS)))
bot.add_handler(MessageHandler(user_details_callback, filters.private))

# Handle callbacks
bot.add_handler(CallbackQueryHandler(callback_query))





