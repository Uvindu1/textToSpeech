from gtts import gTTS # import kara gaththa text to speech module eka
import os

abc = open('simple.txt')
text = abc.read()

language = 'en' # english kiyana eka

obj = gTTS(text = text, lang= language, slow=False)
# mehi slow kiyana eka false demme converted video eka high speed nisa

obj.save("sample.mp3")


os.system("sample.mp3")