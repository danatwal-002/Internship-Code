
import os
from gtts import gTTS

'''
 Make voice more human, here better voice quality but it does TTS on the internet.

'''

text = 'get ready now'
myoutp = gTTS(text=text, lang='en', slow=False)

myoutp.save('talk2.mp3')
os.system('mpg123 talk2.mp3')