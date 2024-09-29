import os
import random
from gtts import gTTS
from playsound import playsound
text="hello world"
acc = 'us'
tts = gTTS(text=text, lang='en', tld=acc)
filename = 'temp.mp3'
tts.save(filename)

playsound(filename)

os.remove(filename)