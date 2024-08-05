
'''
Code for Image Classification using GoogleNet DL model:
[capture from live camera and classify using model]

`ji.detectNet()` --> class for Object Detection tasks.
`ji.imageNet()` --> class for Image Classification tasks

ju.gstCamera(w,h,' ') --> 'dev/video1' for webcam, check if resolution is supported by 
camera, in terminal.
    I used 'csi://0' because it worked. It referes to a camera connected via the CSI (Camera
    Serial Interface) bus, which is a popular interface to connect cameras.

    Jetson Nano has a CSI that allows attaching a CSI camera directly to the board, when 
    using a RPI camera module with Jetson Nano it would typically be connected via the CSI 
    interface.

cam.CaptureRGBA() --> I tried to use `cam.read()` but gave me: 
[ 'jetson.utils.gstCamera' object has no attribute 'read' ], so CaptureRGBA is a
method for gstCamera class (cam instance), captures image frame from camera in 
RGBA32F.

cam.Capture() --> when I tried it, it would give the error "unsupported image format
(nv12)", supported ones are rgb related [including RGBA32F], nv12 is an image format
for storing video or image data.
    By default, Raspberry Pi Camera Module captures video data in the YUV 4:2:0 
    format, which includes NV12 as a common subformat.

classID --> indx of predicted class
GetClassDesc() --> get human-readable label corresp to preicted class indx, from 
googlenet.

'''

import jetson_inference as ji
import jetson_utils as ju
import cv2
import numpy as np

net = ji.imageNet('googlenet')

#intialize camera
cam = ju.gstCamera(640,480) #,"csi://0"

disp = ju.glDisplay() #creating window for displaying camera feed
font = ju.cudaFont() #create font

while disp.IsOpen():

    frame, w,h = cam.CaptureRGBA()
    frame = cv2.cvtColor(frame, cv2.COLOR_YUV2BGR_NV12)

    classID, confidence = net.Classify(frame, w,h) #classifying frame
    item = net.GetClassDesc(classID)
    
    font.OverlayText(frame,w,h,item,5,5,font.Magenta, font.Blue) #label with 'item'
    disp.RenderOnce(frame, w,h)

