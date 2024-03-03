import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import (
    ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
)

load_dotenv()

app = Client(
    'flightssearch_bot',
    api_id = os.environ["TELEGRAM_API_ID"],
    api_hash = os.environ["TELEGRAM_API_HASH"],
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
)

@app.on_callback_query()
async def callback(client, callback_query):
    pages = {
        'page_01': {
            'anterior': InlineKeyboardButton('anterior', callback_data='page_03'),
            'proximo': InlineKeyboardButton('proximo', callback_data='page_02'),
            'texto': 'Você está na page 1'
        },
        'page_02': {
            'proximo': InlineKeyboardButton('proximo', callback_data='page_03'),
            'anterior': InlineKeyboardButton('anterior', callback_data='page_01'),
            'texto': 'Você está na page 2'
        },
        'page_03': {
            'proximo': InlineKeyboardButton('proximo', callback_data='page_01'),
            'anterior': InlineKeyboardButton('anterior', callback_data='page_02'),
            'texto': 'Você está na page 3'
        }
    }
    page = pages[callback_query.data]
    await callback_query.edit_message_text(
        page['texto'],
        reply_markup=InlineKeyboardMarkup([[
            page['anterior'], page['proximo']
        ]])
    )

@app.on_message(filters.command('inline'))
async def inline(client, message):
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Callback', callback_data='page_01'),
                InlineKeyboardButton(
                    'Link',
                    url='https://4llves.dev/'
                )
            ]
        ]
    )
    await message.reply(
        'Entre no meu site',
        reply_markup=buttons
    )

@app.on_message(filters.command('start'))
async def start(client, message):
    teclado = ReplyKeyboardMarkup (
        [
            ['/partida', '/destino']
        ],
        resize_keyboard = True,
    )
    await message.reply(
        'Preciso que responda 5 campos necessários para conseguirmos efetuar a sua pesquisa, clique em um dos botões a baixo e responda de acordo com o solicitado.',
        reply_markup = teclado
    )

@app.on_message(filters.command('help'))
async def help(client, message):
    print(message.chat.username, message.text)
    await message.reply(
        f'Olá {message.chat.username}, sou seu guia para uso do flights search, click em /start para iniciarmos'
    )

@app.on_message(filters.command('chatid'))
async def help(client, message):
    id = message.chat.id
    # print(message.chat.username, message.text)
    await message.reply(
        f'Olá {message.chat.username}, seu chat id e: {id}'
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

# @app.on_message(filters.command('partida'))
# async def partida(client, message):
#     teclado = ReplyKeyboardMarkup (
#         [
#             ['BEL', 'GRU', 'BSB'],
#             ['CGH', 'SSA', 'FLN']
#         ],
#         resize_keyboard = True,
#     )
#     await message.reply(
#         'Selecione um aeroporto de partida ou digite a sigla de 3 digitos.',
#         reply_markup = teclado
#     )

# @app.on_message(filters.command('destino'))
# async def destino(client, message):
#     teclado = ReplyKeyboardMarkup (
#         [
#             ['BEL', 'GRU', 'BSB'],
#             ['CGH', 'SSA', 'FLN']
#         ],
#         resize_keyboard = True,
#     )
#     await message.reply(
#         'Selecione um aeroporto de destino ou digite a sigla de 3 digitos.',
#         reply_markup = teclado
#     )

@app.on_message()
async def message(client, message):
    print(message)
    await message.reply(message.text + '???')

print('Rodando...')
app.run()
