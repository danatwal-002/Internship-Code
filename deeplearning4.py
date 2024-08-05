
import jetson_inference as ji
import jetson_utils as ju
import time
import cv2
import numpy as np

'''
IC

In this code, frames are captured in RGBA format and then converted to BGR format using CUDA and 
OpenCV functions. In the previous code, frames are directly processed from BGR to RGBA format and
then used for classification.

Low resolution image bc it takes the 3264,2464 and crops it to 1280,720

2 ways to launch cam:
  1- using GStreamer (openCV)
  2- using jetson utils

Opposite of deeplearning3.cpp, here latency issues

'''

net = ji.imageNet('googlenet')

width = 1280
height = 720

dispW= width
dispH= height
flip=2

# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

#improved camset:
#camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.2 saturation=1.2 ! appsink'
#cam = cv2.VideoCapture(camSet)

cam = ju.gstCamera(dispW,dispH,'0')

disp = ju.glDisplay()
font1 = ju.cudaFont() 
font = cv2.FONT_HERSHEY_COMPLEX

# net = ji.imageNet('alexnet')

timeM = time.time()
fpsf = 0

while disp.IsOpen():
 
    frame, width, height = cam.CaptureRGBA(zeroCopy=1)

    classID, conf = net.Classify(frame,width,height)
    item = net.GetClassDesc(classID)

    dt = time.time() - timeM #change in time
    fps = 1/dt
    fpsf = .95*fpsf + .05*fps
    timeM = time.time()

    frame = ju.cudaToNumpy(frame, width, height, 4) 
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR).astype(np.uint8) 

    cv2.putText(frame, str(round(fpsf,1))+' fps '+ item, (0,30), font, 1, (0,0,255),2)
    cv2.imshow('wind',frame)
    cv2.moveWindow('wind',0,0) 

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()