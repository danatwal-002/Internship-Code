
import cv2
import numpy as np
import time

'''
 Want to put both frames in same window by stacking them, but need them to be same size
in order to stack horizontally.

 Problem: cameras out of sync (latency)

'''

dispW=640
dispH=480
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)
cam1 = cv2.VideoCapture(1)


font = cv2.FONT_HERSHEY_SIMPLEX

dtav=0
start = time.time()

while True:

    _, frame = cam.read()
    _,frame2 = cam1.read()
    frame2 = cv2.resize(frame2, (frame.shape[1], frame.shape[0]))
    
    # comb = np.hstack((frame,frame2))

    dt = time.time() - start
    dtav = .95*dtav + .5*dt
    fps = 1/dtav

    start = time.time()
    
    cv2.rectangle(comb, (0,0), (100,40),(0,0,255),-1)
    cv2.putText(comb,str(round(fps,1)), (0,25), font, .75, (255,0,255),2)


    # cv2.imshow('rpi', comb)
    cv2.imshow('web', frame)

    # cv2.moveWindow('rpi',0,0)
    cv2.moveWindow('web',600,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
