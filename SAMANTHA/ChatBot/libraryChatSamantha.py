from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement


class Sam_bot:
    nombreBot = ""
    bot = ChatBot("SAM")
    trainer = ChatterBotCorpusTrainer(bot)
    input_statement = Statement(text="Hola")
    def __init__(self, nameBot):
        self.nombreBot = nameBot
        self.bot = ChatBot(
            self.nombreBot,
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'Lo siento, no te he entendido',
                    'maximum_similarity_threshold': 0.75
                },
                {
                    'import_path': 'chatterbot.logic.MathematicalEvaluation'
                }#H,{ 'import_path': 'chatterbot.logic.TimeLogicAdapter'  }
            ]
        )
        self.trainer = ChatterBotCorpusTrainer(self.bot)
        print("Nuevo Bot creado con nombre %s" %nameBot)

    def AprenderIdiomaEspañol(self):
        #self.trainer.train('chatterbot.corpus.spanish.greetings') #un poco de vocabulario
        #self.trainer.train('chatterbot.corpus.spanish.conversations') #algunas conversaciones de ejemplo
        #self.trainer.train('chatterbot.corpus.spanish.trivia') #conversacion fuilda
        self.trainer.train('chatterbot.corpus.spanish')

    def GenerarRespuesta(self, pregunta):
        self.input_statement = Statement(text=pregunta)
        response = self.bot.generate_response(
            self.input_statement
        )
        return response.text

    def RespuestaBot(self, pregunta):
        respuesta = self.bot.get_response(pregunta)
        return respuesta

    def AprenderNuevaRespuesta(self, nuevaRespuesta):
        correct_response = Statement(text=nuevaRespuesta)
        self.bot.learn_response(correct_response, self.input_statement)
        print('Respuesta Aprendida!')

    def ExportTraining(self):
        self.trainer.export_for_training('./training.json')

