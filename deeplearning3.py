
'''
IC

Bad image quality on RPI camera, too low contrast & low saturation, adjust it.

`gst-inspeect-1.0 nvarguscamerasrc` : tells what all the options are on gstreamer, set:
wbmode = 3 (fluorescent, for blue lights)
tnr-mode = 2 (highest qaulity noise reduc)
tnr-strength = 1 (max noise reduction)
ee-mode = 2 (highest qual for sharpening)
sensor-id : which camera
*put spaces not commas between commands/params in GStreamer*
*put spaces between params and !*

latency issues

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
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

#better quality using this:
camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.2 saturation=1.2 ! appsink drop=true'
cam1 = cv2.VideoCapture(camSet)

net = ji.imageNet('googlenet')

font = cv2.FONT_HERSHEY_COMPLEX

timeM = time.time()
fpsf = 0
    
while True:
    ret, frame = cam1.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA).astype(np.float32)
    img = ju.cudaFromNumpy(img)
 
    classID, conf = net.Classify(img,width,height)
    item = ''
    item = net.GetClassDesc(classID)

    dt = time.time() - timeM 
    fps = 1/dt
    fpsf = .95*fpsf + .05*fps
    timeM = time.time()
   
    cv2.putText(frame, str(round(fpsf,1))+' fps '+ item, (0,30), font, 1, (0,0,255),2)
    cv2.imshow('wind',frame)

    cv2.moveWindow('wind',0,0) 

    if cv2.waitKey(1)==ord('q'):
        break

cam1.release()
cv2.destroyAllWindows()