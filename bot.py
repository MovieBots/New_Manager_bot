from pyrogram import Client, filters
from datetime import datetime
import os
import logging
from config import API_ID, API_HASH, TG_BOT_TOKEN, TG_BOT_WORKERS, OWNER_ID, ADMINS

# Its Very Difficult to make this script please arpit pay me 
# Import your handlers
from handlers.start import start_command
from handlers.admin import handle_admin_commands
from handlers.help import help_command
from handlers.premium import buy_premium_command, callback_query
from handlers.user_stats import user_details_callback

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Bot(Client):
    def __init__(self):
        super().__init__(
            "my_bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TG_BOT_TOKEN,
            workers=TG_BOT_WORKERS
        )

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        
        logger.info(f"Bot Running..!\n\nCreated by \n@iTz_Anayokoji")
        logger.info(f"""\n\n
 █████╗ ███╗   ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗
██╔══██╗████╗  ██║██║██╔════╝██║  ██║██║████╗  ██║
███████║██╔██╗ ██║██║███████╗███████║██║██╔██╗ ██║
██╔══██║██║╚██╗██║██║╚════██║██╔══██║██║██║╚██╗██║
██║  ██║██║ ╚████║██║███████║██║  ██║██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝                 
                                   
                                    """)

    def run(self):
        self.add_handler(filters.command("start")(start_command))
        self.add_handler(filters.private & filters.text(handle_admin_commands))
        self.add_handler(filters.command("help")(help_command))
        self.add_handler(filters.command("buy_premium")(buy_premium_command))
        self.add_handler(filters.callback_query()(callback_query))
        self.add_handler(filters.callback_query(filters.regex(r"user_details_\d+"))(user_details_callback))
        super().run()

if __name__ == "__main__":
    bot = Bot()
    bot.run()


