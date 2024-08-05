
'''
contours = set of x,y pts that define the outline of one obj of interest
contour command returns array that might have many set of pts [cnt1, cnt2,....]
each cnt has (x,y) pts

we have prob:
noise, we have cnts being generated in random order, not necessarily the ones we 
care about --> sort cnts, then we can show first cnt (biggest one)

what if i have multp objs to track: for loop

#tracking with rectangle looks better
'''

import cv2
print(cv2.__version__)
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)

cv2.createTrackbar('hueLower', 'Trackbars',50,179,nothing)
cv2.createTrackbar('hueUpper', 'Trackbars',100,179,nothing)

cv2.createTrackbar('hue2Lower', 'Trackbars',50,179,nothing)
cv2.createTrackbar('hue2Upper', 'Trackbars',100,179,nothing)

cv2.createTrackbar('satLow', 'Trackbars',100,255,nothing)
cv2.createTrackbar('satHigh', 'Trackbars',255,255,nothing)
cv2.createTrackbar('valLow','Trackbars',100,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)


dispW=640
dispH=480
flip=4

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

while True:
    ret, frame = cam.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hueLow=cv2.getTrackbarPos('hueLower', 'Trackbars')
    hueUp=cv2.getTrackbarPos('hueUpper', 'Trackbars')

    hue2Low=cv2.getTrackbarPos('hue2Lower', 'Trackbars')
    hue2Up=cv2.getTrackbarPos('hue2Upper', 'Trackbars')

    Ls=cv2.getTrackbarPos('satLow', 'Trackbars')
    Us=cv2.getTrackbarPos('satHigh', 'Trackbars')

    Lv=cv2.getTrackbarPos('valLow', 'Trackbars')
    Uv=cv2.getTrackbarPos('valHigh', 'Trackbars')

    l_b=np.array([hueLow,Ls,Lv])
    u_b=np.array([hueUp,Us,Uv])

    l_b2=np.array([hue2Low,Ls,Lv])
    u_b2=np.array([hue2Up,Us,Uv])

    FGmask=cv2.inRange(hsv,l_b,u_b)
    FGmask2=cv2.inRange(hsv,l_b2,u_b2)
    FGmaskComp=cv2.add(FGmask,FGmask2) #mask to generate contours

    #create contour

    contours, _ = cv2.findContours(FGmaskComp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    
    #returns 2 param, 1st is an array of lists/sets
    #find cnts based on mask not img
    #RETR_EXTERNAL : to retreive external pts
    #CHAIN_APPROX_SIMPLE: simplified set of x,y which outline my obj of interest in mask
    
    #sol
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
    #draw every cnt that has an area >=50, to track more than one obj
    for i in contours:
        area = cv2.contourArea(i) #find area of each cnt
        (x,y,w,h) = cv2.boundingRect(i)
        if area>=50:
           # cv2.drawContours(frame, [i], 0, (255,0,0),3) #-1 draw all cnts, 0 draws first
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)

    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0)

    cv2.imshow('FGmaskComp',FGmaskComp)
    cv2.moveWindow('FGmaskComp',0,530)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()