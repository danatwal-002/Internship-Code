

import cv2
import numpy as np

cv2.namedWindow('name')
cv2..moveWIndow('name',1320,0)
cv2.imshow('name')

dispW=640
dispH=480
flip=4

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#cam=cv2.VideoCapture(0)

while True:

    ret, frame = cam.read()
    frame = cv2.imread(r'/home/sul/Downloads/smarties.png')
   
    # cv2.imshow('im',img)
    
    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0) #move camera to upper left corner

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
