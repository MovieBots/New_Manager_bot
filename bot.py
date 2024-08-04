# Don't change any think here this is important part 

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from datetime import datetime
import logging
from config import API_ID, API_HASH, TG_BOT_TOKEN, TG_BOT_WORKERS, OWNER_ID, ADMINS

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
        # Register handlers
        self.add_handler(MessageHandler(start_command, filters.command("start")))
        self.add_handler(MessageHandler(handle_admin_commands, filters.private & filters.text))
        self.add_handler(MessageHandler(help_command, filters.command("help")))
        self.add_handler(MessageHandler(buy_premium_command, filters.command("buy_premium")))
        self.add_handler(CallbackQueryHandler(callback_query))
        self.add_handler(CallbackQueryHandler(user_details_callback, filters.regex(r"user_details_\d+")))

        # Start the bot
        self.start()
        # Run the bot's idle loop
        self.idle()

if __name__ == "__main__":
    bot = Bot()
    bot.run()



