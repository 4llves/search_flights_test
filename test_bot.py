import os
from dotenv import load_dotenv
import telebot

load_dotenv()

"""
    /destino informe o aeroporto de embarque
    /data_de_partida informe a data do voo de partida
    /data_de_volta informe a data do voo de volta
"""

token = os.environ["token_telegram"]
bot = telebot.TeleBot(token)
url_base = f'api.telegram.org/bot{token}'

# def msg_obtain(update_id):    
#     msg_capture = f'{url_base}/getUpdates?timeout=100'
#     if update_id:
#         msg_capture = f'{msg_capture}/&offset={update_id + 1}'
#     result = resquests.get(msg_capture)
#     print(result)

@bot.message_handler(commands=["iniciar"])
def start(msg):
    text = """
        Vou lhe perguntar alguns dados do voo, por favor responda de acordo com os exemplos.
        Clique no embarque para começarmos:
        /embarque"""
    
    bot.send_message(msg.chat.id, text)

@bot.message_handler(commands=["embarque"])
def start(msg):
    text_info = """Digite as siglas do aeroporto de Embarque. Ex: Digite BEL para Belém ou GRU para Guarulhos"""

    bot.reply_to(msg, text_info)

@bot.message_handler(commands=["destino"])
def start(msg):
    departures = msg.text
    bot.reply_to(msg, "Digite as siglas do aeroporto de Destino. Ex: Digite BEL para Belém ou GRU para Guarulhos")
    
    msg_obtain()

# @bot.message_handler(commands=["data_de_partida"])
# def start(msg):
#     bot.reply_to(msg, "Digite a data de partida. Ex: 01/01/2024")

# @bot.message_handler(commands=["data_de_volta"])
# def start(msg):
#     bot.reply_to(msg, "Digite a data de partida. Ex: 31/12/2024")

def verify(msg):    
    return True

@bot.message_handler(func=verify)
def response(msg):    
    user = msg.chat.first_name
    text_info = f"""
    Olá {user}, sou o Flights Search, seu bot para encontrar passagens a custo benefício 😉:        
    Responder qualquer outra coisa estará sujeito a falhas. Clique na opção de iniciar.
    /iniciar"""

    bot.reply_to(msg, text_info)

bot.polling()