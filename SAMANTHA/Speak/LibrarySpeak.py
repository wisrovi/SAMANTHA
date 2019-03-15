import win32com.client as wincl


speak = wincl.Dispatch("SAPI.SpVoice")

class SpeakSAM:
    def talking(self, text):
        audio = speak.Speak(text)
