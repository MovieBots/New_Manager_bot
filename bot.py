from pyrogram import Client, filters
from datetime import datetime
import os
from config import API_ID, API_HASH, TG_BOT_TOKEN, TG_BOT_WORKERS, OWNER_ID, ADMINS

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
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TG_BOT_TOKEN,
            workers=TG_BOT_WORKERS
        )

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        
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
        self.add_handler(Client.on_message(filters.command("start"))(start_command))
        self.add_handler(Client.on_message(filters.private & filters.text)(handle_admin_commands))
        self.add_handler(Client.on_message(filters.command("help"))(help_command))
        self.add_handler(Client.on_message(filters.command("buy_premium"))(buy_premium_command))
        self.add_handler(Client.on_callback_query()(callback_query))
        self.add_handler(Client.on_callback_query(filters.regex(r"user_details_\d+"))(user_details_callback))
        super().run()

if __name__ == "__main__":
    bot = Bot()
    bot.run()

