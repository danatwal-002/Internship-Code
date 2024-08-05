
import jetson_inference as ji
import jetson_utils as ju
import time
import cv2
import numpy as np

net = ji.detectNet('ssd-mobilenet-v2',threshold=0.5)

width = 1280
height = 720
dispW = width
dispH = height
flip=2

camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.2 saturation=1.2 ! appsink drop=true'
cam = cv2.VideoCapture(camSet)

font = cv2.FONT_HERSHEY_COMPLEX

t,b,r,l = 0,0,0,0
text = ' '
while True:
    
    _, img = cam.read()
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    frame = ju.cudaFromNumpy(frame)
    
    tk=1

    dets = net.Detect(frame)
    for d in dets:
        t,b,r,l = int(d.Top), int(d.Bottom), int(d.Right), int(d.Left)
        print(t,b,l)
        id = d.ClassID
        item = net.GetClassDesc(id)
        text = item

        if text == 'cat': #blocking cat from view
            tk=-1
    
    cv2.rectangle(img, (l,t), (r,b), (255,0,0),tk)
    cv2.putText(img, text, (l,t+20), font, .75, (0,0,255),2)

    cv2.imshow('img',img)
    cv2.moveWindow('img',0,0) 

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()