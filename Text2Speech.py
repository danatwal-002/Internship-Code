
import os
import pyttsx3

'''
 Text2Speech: need sound device on JN, like speakers in monitor.

 pyttsx3 can use 'espeak' as one of its available TTS engines if espeak is intsalled in
system.


'''

#create speech engine:
engine = pyttsx3.init(driverName='espeak')

#slow down
engine.setProperty('rate',150)

#change voice, m for male, f for female, there are 4 voices
engine.setProperty('voice', 'english+m1')

#text to say:
text = 'hello'

#create sound:
engine.say(text)

#play sound:
engine.runAndWait()
