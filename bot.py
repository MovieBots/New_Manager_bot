import logging
import os
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_BOT_WORKERS = int(os.getenv("TG_BOT_WORKERS", "4"))
OWNER_ID = int(os.getenv("OWNER_ID"))
ADMINS = [int(admin) for admin in os.getenv("ADMINS", "").split(",")]

logging.basicConfig(level=logging.INFO)

async def start_command(client, message):
    await message.reply(
        "Yo what's up\n\nI am a membership provider bot by Arpit.",
        parse_mode='markdown'
    )

class Bot(Client):
    def __init__(self):
        super().__init__(
            "my_bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TG_BOT_TOKEN,
            workers=TG_BOT_WORKERS
        )
        self.LOGGER = logging.getLogger(__name__)

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        self.set_parse_mode("html")
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
        self.add_handler(MessageHandler(start_command, filters.command("start")))
        super().run()

    async def stop(self):
        await super().stop()
        self.LOGGER.info("Bot stopped. Bye!")

if __name__ == "__main__":
    bot = Bot()
    bot.run()





