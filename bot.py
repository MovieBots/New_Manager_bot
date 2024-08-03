from pyrogram import Client, filters, ParseMode
from pyrogram.types import Message
from datetime import datetime
import os
import sys

# Import your handlers
from handlers.start import start_command
from handlers.admin import handle_admin_commands
from handlers.help import help_command
from handlers.premium import buy_premium_command, callback_query
from handlers.user_stats import user_details_callback

class Bot(Client):
    def __init__(self):
        super().__init__(
            "my_bot",
            api_id=os.getenv("API_ID"),
            api_hash=os.getenv("API_HASH"),
            bot_token=os.getenv("TG_BOT_TOKEN"),
            workers=int(os.getenv("TG_BOT_WORKERS", "4"))
        )

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER.info(f"Bot Running..!\n\nCreated by \n@iTz_Anayokoji")
        self.LOGGER.info(f"""\n\n
 █████╗ ███╗   ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗
██╔══██╗████╗  ██║██║██╔════╝██║  ██║██║████╗  ██║
███████║██╔██╗ ██║██║███████╗███████║██║██╔██╗ ██║
██╔══██║██║╚██╗██║██║╚════██║██╔══██║██║██║╚██╗██║
██║  ██║██║ ╚████║██║███████║██║  ██║██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝                 
                                   
                                    """)
    
    def run(self):
        self.add_handler(filters.command("start")(start_command))
        self.add_handler(filters.private & filters.text()(handle_admin_commands))
        self.add_handler(filters.command("help")(help_command))
        self.add_handler(filters.command("buy_premium")(buy_premium_command))
        self.add_handler(filters.callback_query()(callback_query))
        self.add_handler(filters.callback_query(filters.regex(r"user_details_\d+"))(user_details_callback))
        super().run()

if __name__ == "__main__":
    bot = Bot()
    bot.run()
