
import jetson_inference as ji
import jetson_utils as ju
import cv2
import numpy as np
import os
from gtts import gTTS
import threading 

speak=True
item='welcome'
conf=0
itemold = ''

w=1280
h=720
dispW=w
dispH=h
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
 
net =ji.imageNet('googlenet')
font = cv2.FONT_HERSHEY_COMPLEX

def say():
    global speak 
    global item
    while True:
        if speak == True:
            outp = gTTS(text=item,lang='en', slow=False)
            outp.save('outp.mp3')
            os.system('mpg123 outp.mp3')
            speak = False
x = threading.Thread(target=say, daemon=True)
x.start()        

while True:

    ret, frame = cam.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA).astype(np.float32)
    img = ju.cudaFromNumpy(img)
    
    if speak == False:

        classid,conf = net.Classify(img,w,h)
        if conf >= .5:
            item = net.GetClassDesc(classid)
            if item != itemold:
                speak=True
        if conf < .5:
            item=''
        itemold=item    

    cv2.putText(frame, str(round(conf,1))+ item, (0,30), font,.75,(255,0,0),1)
    
    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0) 
   
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()