from asyncio import run
import os
from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()

app = Client(
    'flightssearch_bot',
    api_id = os.environ["TELEGRAM_API_ID"],
    api_hash = os.environ["TELEGRAM_API_HASH"],
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
)

async def main():    
    await app.start()
    await app.send_message(
        'Alves_dev', 'Hello World 😎'
    )
    await app.stop()

run(main())