import speech
speech.say('Hola mundo', 'es_ES')
text = speech.recognize('audio.m4a', 'en')[0][0]  # sent to Apple servers
print(text)