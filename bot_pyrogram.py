import os
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

app = Client(
    'flightssearch_bot',
    api_id = os.environ["TELEGRAM_API_ID"],
    api_hash = os.environ["TELEGRAM_API_HASH"],
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
)

@app.on_message(filters.command('help'))
async def help(client, message):
    print(message.chat.username, message.text)
    await message.reply(
        f'Olá {message.chat.username}, sou seu guia para uso do flights search'
    )

@app.on_message()
async def message(client, message):
    print(message.chat.username, message.text)
    await message.reply(message.text + '???')

app.run()