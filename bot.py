import logging
import sys
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from datetime import datetime
from config import API_HASH, API_ID, TG_BOT_TOKEN, TG_BOT_WORKERS, PORT
from pyrogram.errors import FloodWait
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={
                "root": "plugins"  # Ensure this points to the correct plugins directory
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        while True:
            try:
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
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝                 
                                   
                                    """)
                self.username = usr_bot_me.username
                break
            except FloodWait as e:
                LOGGER.warning(f"FloodWait: Waiting for {e.x} seconds.")
                time.sleep(e.x)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped.")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
