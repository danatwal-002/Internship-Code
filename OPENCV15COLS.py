

import cv2
import numpy as np

dispW=640
dispH=480
flip=4

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

blank = np.zeros((480,640,1), np.uint8)
blank[:] = 8

while True:

    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0) 

    # b = cv2.split(frame)[0]
    # g = cv2.split(frame)[1]
    # r = cv2.split(frame)[2]
    
    b,g,r = cv2.split(frame)

    g[:] = g[:]*0.2
    r[:] = r[:]*0.25

    blue = cv2.merge((b,blank,blank))
    green = cv2.merge((blank,g,blank))
    red = cv2.merge((blank,blank, r))

    merge = cv2.merge((b,g,r))
    # m =  cv2.merge((g,b,r))

    cv2.imshow('b',g)
    cv2.moveWindow('b',0,500)

    # cv2.imshow('bl',blue)
    # cv2.moveWindow('bl',0,500)

    cv2.imshow('gl',green)
    cv2.moveWindow('gl',500,0)

    # cv2.imshow('merge',merge)
    # cv2.moveWindow('merge',500,0)

    # cv2.imshow('m',m)
    # cv2.moveWindow('m',500,0)

    key = cv2.waitKey(1)
    if key==ord('q'):
        break
    
    #print(frame.shape)
    if key==ord('o'):
        # print(gray.shape)
        # print('# of pixels = ',gray.size) #640*480
        # print('# of pixels in frame = ', frame.size)
        print(frame[50,45,0]) #pix at r 45 and col 50, green.


   

cam.release()
cv2.destroyAllWindows()
