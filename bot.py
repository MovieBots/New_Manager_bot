import logging
from aiohttp import web
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from config import API_HASH, API_ID, TG_BOT_TOKEN, TG_BOT_WORKERS, PORT


# Set up logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        try:
            self.set_parse_mode(ParseMode.HTML)
            self.LOGGER.info(
                f"Bot Running..!\n\nCreated by \n@iTz_Anayokoji")
            self.LOGGER.info(f""" \n\n
        
 █████╗ ███╗   ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗
██╔══██╗████╗  ██║██║██╔════╝██║  ██║██║████╗  ██║
███████║██╔██╗ ██║██║███████╗███████║██║██╔██╗ ██║
██╔══██║██║╚██╗██║██║╚════██║██╔══██║██║██║╚██╗██║
██║  ██║██║ ╚████║██║███████║██║  ██║██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝                 
                                   
                                    """)
            self.username = usr_bot_me.username

            # web-response
            app = web.AppRunner(await web_server())
            await app.setup()
            bind_address = "0.0.0.0"
            await web.TCPSite(app, bind_address, PORT).start()
        except Exception as e:
            self.LOGGER.warning(e)
            self.LOGGER.warning("Failed to start the bot properly.")
            sys.exit()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped.")

# Initialize and run the bot
app = Bot()
app.run()
