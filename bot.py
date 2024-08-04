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

# Import handlers
from handlers.start import start_command
from handlers.help import help_command
from handlers.premium import buy_premium_command, callback_query
from handlers.admin import handle_admin_commands
from handlers.user_stats import user_details_callback

class Bot(Client):
    def __init__(self):
        super().__init__(
            "bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TG_BOT_TOKEN,
            workers=TG_BOT_WORKERS
        )
        self.uptime = None

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        
        logging.info(f"Bot Running..!\n\nCreated by \n@iTz_Anayokoji")
        logging.info(f"""\n\n
 █████╗ ███╗   ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗
██╔══██╗████╗  ██║██║██╔════╝██║  ██║██║████╗  ██║
███████║██╔██╗ ██║██║███████╗███████║██║██╔██╗ ██║
██╔══██║██║╚██╗██║██║╚════██║██╔══██║██║██║╚██╗██║
██║  ██║██║ ╚████║██║███████║██║  ██║██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝                 
        """)
        
    def run(self):
        self.add_handler(MessageHandler(start_command, filters.command("start")))
        self.add_handler(MessageHandler(help_command, filters.command("help")))
        self.add_handler(MessageHandler(buy_premium_command, filters.command("buy_premium")))
        self.add_handler(MessageHandler(handle_admin_commands, filters.command(["add_user", "remove_user", "stats"])))
        self.add_handler(MessageHandler(user_details_callback, filters.create(lambda _, __, query: query.data.startswith("user_details_"))))

        super().run()

if __name__ == "__main__":
    bot = Bot()
    bot.run()




