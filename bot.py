import logging
from aiohttp import web
from pyrogram import Client
from config import API_HASH, API_ID, TG_BOT_TOKEN, TG_BOT_WORKERS, PORT

# Set up logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=TG_BOT_TOKEN,
            workers=TG_BOT_WORKERS
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        self.uptime = datetime.now()
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER.info(f"Bot Running..!\n\nCreated by \n@iTz_Anayokoji")

        # Web server setup (if needed)
        # app = web.AppRunner(await web_server())
        # await app.setup()
        # bind_address = "0.0.0.0"
        # await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped.")
