import logging
import sys
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from datetime import datetime
from config import API_HASH, API_ID, TG_BOT_TOKEN, TG_BOT_WORKERS, PORT, OWNER_ID, ADMINS
from aiohttp import web
from web_server import web_server
from database.database import load_admin_ids, save_admin_ids
from handlers import admin, help, premium, start, user_stats

# Load admin IDs from the database
admin_ids = load_admin_ids()
premium_users = {}

# Set up logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

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
        self.username = usr_bot_me.username
        app = web.AppRunner(await web_server())
        await app.setup()
        site = web.TCPSite(app, "0.0.0.0", PORT)
        await site.start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped")

    async def on_start(self):
        self.LOGGER.info("Bot started successfully")

# Initialize the bot
bot = Bot()

# Add handlers
bot.add_handler(filters.command("start") & filters.private, start.start_command)
bot.add_handler(filters.command("help") & filters.private, help.help_command)
bot.add_handler(filters.command(["add_user", "remove_user", "stats"]) & filters.private, admin.handle_admin_commands)
bot.add_handler(filters.command("buy_premium") & filters.private, premium.buy_premium_command)
bot.add_handler(filters.callback_query, premium.callback_query)
bot.add_handler(filters.callback_query, user_stats.user_details_callback)

if __name__ == "__main__":
    bot.run()
