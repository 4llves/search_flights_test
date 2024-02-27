import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

load_dotenv()

app = Client(
    'flightssearch_bot',
    api_id = os.environ["TELEGRAM_API_ID"],
    api_hash = os.environ["TELEGRAM_API_HASH"],
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
)

@app.on_message(filters.command('teclado'))
async def teclado(client, message):
    teclado = ReplyKeyboardMarkup (
        [
            ['/partida', '/destino']
        ],
        resize_keyboard = True,
    )
    await message.reply(
        'Aperta aí no teclado',        
        reply_markup = teclado
    )

@app.on_message(filters.command('partida'))
async def partida(client, message):
    teclado = ReplyKeyboardMarkup (
        [
            ['BEL', 'GRU', 'BSB'],
            ['CGH', 'SSA', 'FLN']
        ],
        resize_keyboard = True,
    )
    await message.reply(
        'Selecione um aeroporto de partida ou digite a sigla de 3 digitos.',
        reply_markup = teclado
    )

@app.on_message(filters.command('destino'))
async def destino(client, message):
    teclado = ReplyKeyboardMarkup (
        [
            ['BEL', 'GRU', 'BSB'],
            ['CGH', 'SSA', 'FLN']
        ],
        resize_keyboard = True,
    )
    await message.reply(
        'Selecione um aeroporto de destino ou digite a sigla de 3 digitos.',
        reply_markup = teclado
    )

@app.on_message(filters.audio | filters.voice)
async def help(client, message):    
    await message.reply(
        'Descuple, mas não consigo processar audios. Tente usar o comando /help para mais informações.'
    )

@app.on_message(filters.sticker | filters.photo | filters.video)
async def help(client, message):    
    await message.reply(
        'Descuple, mas não consigo processar imagens ou videos. Tente usar o comando /help para mais informações.'
    )

@app.on_message(filters.command('help'))
async def help(client, message):
    print(message.chat.username, message.text)
    await message.reply(
        f'Olá {message.chat.username}, sou seu guia para uso do flights search'
    )

@app.on_message(filters.text == 'BEL')
async def message(client, message):    
    teclado = ReplyKeyboardMarkup (
        [
            ['SIM', 'NÃO']
        ],
        resize_keyboard = True,
    )
    await message.reply(
        'Você selecinou aeroporto de Belém, desejas confirmar?'        
    )

@app.on_message(filters.text == 'SIM')
async def message(client, message):    
    await message.reply(
        'Irei registrar, podes passar para o próximo comando.'
    )

@app.on_message()
async def message(client, message):
    print(message.chat.username, message.text)
    await message.reply(message.text + '???')

print('Rodando...')
app.run()
