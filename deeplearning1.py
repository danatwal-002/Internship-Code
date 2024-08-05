
'''
Code for Image Classification on live video using GoogleNet NN
Using ju & ji libraries for these tasks on an NVIDIA Jetson device.

Image Recognition: show obj and detects.

Set spicific values for w,h not randomly

Change the display window because it takes whole screen & shows img as smaller:
Idea: trying to display with OpenCV --> coment disp

zeroCopy=1 --> don't move image into many locations, have just one place and reference
that one place in memory, needed for conversion from  RGBA to BGR for openCV display.

'''


import jetson_inference as ji
import jetson_utils as ju
import time
import cv2
import numpy as np


width = 1280
height = 720

dispW= width
dispH= height
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam1 = cv2.VideoCapture(camSet)

# cam = ju.gstCamera(dispW,dispH,'0')

disp = ju.glDisplay() #create display window for displaying video frames & classif results
font1 = ju.cudaFont() 
net = ji.imageNet('googlenet') #obj for IC using GoogleNet

font = cv2.FONT_HERSHEY_COMPLEX

timeM = time.time()
fpsf = 0

while disp.IsOpen():
    ret, frame = cam1.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA).astype(np.float32)
    img = ju.cudaFromNumpy(img)
 
    # frame, width, height = cam.CaptureRGBA(zeroCopy=1)

    classID, conf = net.Classify(img,width,height)
    item = ''
    item = net.GetClassDesc(classID)
    dt = time.time() - timeM #change in time
    fps = 1/dt
    
    #get rid of noise
    fpsf = .95*fpsf + .05*fps
    timeM = time.time()
    # font1.OverlayText(frame, width, height, str(round(fpsf,1))+'fps'+ item,5,5,font1.Blue,font1.Purple)

    # disp.RenderOnce(frame, width,height)

    #convert from cuda(RGBA, has 4 nums so 4 params) to np
    # frame = ju.cudaToNumpy(frame, width, height, 4) #4 is for the A in RGBA

    #now we are in numpy format but still in RGBA 
    # frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR).astype(np.uint8) #cuda is float
    cv2.putText(frame, str(round(fpsf,1))+' fps '+ item, (0,30), font, 1, (0,0,255),2)
    cv2.imshow('wind',frame)

    cv2.moveWindow('wind',0,0) 

    if cv2.waitKey(1)==ord('q'):
        break

cam1.release()
cv2.destroyAllWindows()