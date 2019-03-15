import telebot
from telebot import types

from threading import Thread

class ComandReceivedTelegram():
    tb = None

    def __init__(self, Token):
        Thread(self.bucleInfinito(Token))

    def bucleInfinito(self, Token):
        self.tb = telebot.TeleBot(Token)

        @self.tb.message_handler(commands=['start'])
        def send_welcome(message):
            cid = message.chat.id
            self.tb.reply_to(message, "Hola!, soy el bot de la FCV, "
                                 "por favor digite su numero de documento "
                                 "despues del comando /DOC para registrarlo en la DB")

        @self.tb.message_handler(commands=['DOC'])
        def comando_doc(mensaje):
            chat_id = mensaje.chat.id
            unique_code = self.extract_unique_code(mensaje.text)
            print(unique_code)

        @self.tb.message_handler(function=lambda message:True)
        def message(message):
            print("hello")
            self.tb.reply_to(message,message.text)

        def listener(message):
            for m in message:
                chat_id = m.chat.id
                texto = m.text
                self.tb.reply_to(m, texto)

        self.tb.set_update_listener(listener)
        self.tb.polling()

    def extract_unique_code(self, text):
        mensaje_filtrado = text.split()
        contadorItemsLista = 0
        for item in mensaje_filtrado:
            contadorItemsLista += 1

        if contadorItemsLista > 1:
            return mensaje_filtrado[1]
        else:
            return " "