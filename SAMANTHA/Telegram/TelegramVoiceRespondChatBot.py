from SAMANTHA.Speak.LibrarySpeakWithExport import *

voiceSAM = SpeakSAM()

import telebot

from SAMANTHA.ChatBot.libraryChatSamantha import *
SAM = Sam_bot("SAMANTHA")
SAM.AprenderIdiomaEspañol()


class ComandReceivedTelegram():
    tb = None
    UsarAudio = False

    def __init__(self, Token):
        self.tb = telebot.TeleBot(Token)

        @self.tb.message_handler(commands=['help'])
        def send_welcome(message):
            cid = message.chat.id
            self.tb.reply_to(message, "\n /start iniciar conversación con servidor"
                                      "\n /help ayuda sobre comandos"
                                      "\n /DOC para registrarse en la DB"
                                      "\n /AUDIO_ON : encender la respuesta por voz"
                                      "\n /AUDIO_OFF : apagar la respuesta por voz")

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

        @self.tb.message_handler(commands=['AUDIO_ON'])
        def comando_doc(mensaje):
            chat_id = mensaje.chat.id
            unique_code = self.extract_unique_code(mensaje.text)
            self.UsarAudio = True

        @self.tb.message_handler(commands=['AUDIO_OFF'])
        def comando_doc(mensaje):
            chat_id = mensaje.chat.id
            unique_code = self.extract_unique_code(mensaje.text)
            self.UsarAudio = False

        @self.tb.message_handler(function=lambda message:True)
        def message(message):
            nombreArchivoResultante = voiceSAM.convertirTextoVoz(message.chat.id, message.text)
            print(nombreArchivoResultante)
            if nombreArchivoResultante != None:
                self.tb.send_audio(chat_id=message, audio=open(nombreArchivoResultante, 'rb'))
                voiceSAM.borrarAudio()
            else:
                self.tb.reply_to(message, message.text)

        def listener(message):
            for m in message:
                chat_id = m.chat.id
                texto = m.text

                respuestaChatBot = SAM.GenerarRespuesta(texto)

                if self.UsarAudio == False:
                    self.tb.reply_to(m, respuestaChatBot)
                else:
                    nombreArchivoResultante = voiceSAM.convertirTextoVoz(str(chat_id), respuestaChatBot)

                    print(nombreArchivoResultante)
                    if nombreArchivoResultante != None:
                        self.tb.send_audio(chat_id=chat_id, audio=open(nombreArchivoResultante, 'rb'))
                        voiceSAM.borrarAudio()
                        print("audio")
                    else:
                        print("no audio")
                        self.tb.reply_to(m, respuestaChatBot)


        print("Sistema listo para recibir mensajes")
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


