from pyrogram import Client

app = Client("my_bot", api_id="your_api_id", api_hash="your_api_hash", bot_token="your_bot_token")

if __name__ == "__main__":
    # Set up webhook or run bot
    app.run()
