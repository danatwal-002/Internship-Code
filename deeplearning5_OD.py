
'''
Simple code.

Object Detection: recognizes objs & gives location of them by drawing a BB.

w & h (in while loop) are the width & height of the frame so can't control window.

'''


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
flip = 2

cam = ju.gstCamera(dispW,dispH,'0')
disp = ju.glDisplay()

font1 = ju.cudaFont() 
font = cv2.FONT_HERSHEY_COMPLEX

start = time.time()
fpsf = 0

while disp.IsOpen():

    img,w,h = cam.CaptureRGBA()
    dets = net.Detect(img,w,h)
    disp.RenderOnce(img,w,h)
    
    dt=time.time()-start
    start = time.time()
    fps=1/dt
    fpsf=.9*fpsf +.1*fps
    print(str(round(fpsf,1))+'fps')
    
