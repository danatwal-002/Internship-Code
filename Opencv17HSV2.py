
import cv2
import numpy as np

def nth(x):
    pass
'''
we fine-tune hue to get col we need, 
hue val --> [0,179]
sat val --> [0,255] --> 255 sat val --> pure/intense pigment
value val --> add black --> 0 value val --> get black
                        --> top val is white, and middle val is gray.

set HL,SL,VL on lowest val and HU,SU,VU on highest val to see clear img
'''

cv2.namedWindow('bar')
cv2.moveWindow('bar',1300,0)

#need 6 trackbars
cv2.createTrackbar('hueL', 'bar',50,179,nth)
cv2.createTrackbar('hueH', 'bar',100,179, nth)

cv2.createTrackbar('satL', 'bar',100,255,nth)
cv2.createTrackbar('satH', 'bar',255,255, nth)

cv2.createTrackbar('valL', 'bar',100,255,nth)
cv2.createTrackbar('valH', 'bar',255,255, nth)

cv2.createTrackbar('HLred', 'bar',100,179,nth)
cv2.createTrackbar('HUred', 'bar',100,179, nth)

#no need for imshow here because we created it with a window.

dispW=640
dispH=480
flip=4

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

while True:

    ret, frame = cam.read()
    # frame = cv2.imread(r'/home/sul/Downloads/smarties.png') #in RGB col space

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # cv2.imshow('nanocam',fr)
    # cv2.moveWindow('nanocam',0,0) 

    #reading them:
    hueL = cv2.getTrackbarPos('hueL','bar')
    hueH = cv2.getTrackbarPos('hueH','bar')

    satL = cv2.getTrackbarPos('satL','bar')
    satH = cv2.getTrackbarPos('satH','bar')

    Lv = cv2.getTrackbarPos('valL','bar')
    Hv = cv2.getTrackbarPos('valH','bar')

    hueUred = cv2.getTrackbarPos('HUred','bar')
    hueLred = cv2.getTrackbarPos('HLred','bar')

    lb = np.array([hueL, satL, Lv])
    ub = np.array([hueH, satH, Hv])

    lb2 = np.array([hueLred, satL, Lv])
    ub2 = np.array([hueUred, satH, Hv])

    # print(lb,',', ub)
    fg = cv2.inRange(hsv, lb, ub) #color thresholding, pix in range --> set to white
    #pix out range --> swet to black (zero)
    fg2 = cv2.inRange(hsv, lb2, ub2)

    FGim = cv2.bitwise_and(frame,frame, mask=fg)

    fgmaskComp = cv2.add(fg, fg2)
    FGim2 = cv2.bitwise_and(frame,frame, mask=fgmaskComp)


    # BGim = cv2.bitwise_not(fg)
    BGim = cv2.bitwise_not(fgmaskComp)

    bg = cv2.cvtColor(BGim, cv2.COLOR_GRAY2BGR)

    final = cv2.add(FGim, bg)

    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0)

    # cv2.imshow('fgmask',fg)
    # cv2.moveWindow('fgmask',500,0)

    # cv2.imshow('fgim',FGim)
    # cv2.moveWindow('fgim',500,0)

    # cv2.imshow('bgim',BGim)
    # cv2.moveWindow('bgim',500,500)

    cv2.imshow('f',final)
    cv2.moveWindow('f',0,1000)

    cv2.imshow('fgmaskComp',fgmaskComp)
    cv2.moveWindow('fgmaskComp',500,0)
 
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()