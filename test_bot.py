import os
from dotenv import load_dotenv
import telebot

load_dotenv()

token = os.environ["token_telegram"]
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, "Vou lhe perguntar alguns dados do voo, por favor responda de acordo com os exemplos")

def vefiry(msg):    
    return True

@bot.message_handler(func=vefiry)
def response(msg):
    texto = """
    Olá, sou o Flights Search, seu bot para encontrar passagens a custo benefício ^^:
        /start inicia a inserção de dados
    Responder qualquer outra coisa não vai funcionar. Clique na opção de inicio."""

    bot.reply_to(msg, texto)

bot.polling()