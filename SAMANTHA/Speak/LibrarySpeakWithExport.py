from gtts import gTTS

import os
import os.path as path

class SpeakSAM:
    rutaArchivo = ""

    def __init__(self):
        self.crearCarpetaSiNoExiste()

    def convertirTextoVoz(self, nombreArchivo, texto):
        tts = gTTS(text=texto, lang='es')
        self.rutaArchivo = "audiosEnviados/" + nombreArchivo + ".mp3"
        tts.save(self.rutaArchivo)
        if path.exists(self.rutaArchivo):
            return self.rutaArchivo
        else:
            return None

    def borrarAudio(self):
        os.system("rm -rf " + self.rutaArchivo)

    def crearCarpetaSiNoExiste(self):
        nombreCarpeta = "audiosEnviados/"
        if path.exists(nombreCarpeta):
            print("Directorio listo para el almacenamiento de audios")
        else:
            os.mkdir(nombreCarpeta)
            print("Directorio para audios creado correctamente.")