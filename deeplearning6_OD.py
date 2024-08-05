
import jetson_inference as ji
import jetson_utils as ju
import time
import cv2
import numpy as np


'''
 Object Detection: not simple version


'''

net = ji.detectNet('ssd-mobilenet-v2',threshold=0.5)

width = 1280
height = 720
dispW = width
dispH = height
flip=2

camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.2 saturation=1.2 ! appsink drop=true'
cam = cv2.VideoCapture(camSet)

#cam = ju.gstCamera(dispW,dispH,'0')
#disp = ju.glDisplay()

font1 = ju.cudaFont() 
font = cv2.FONT_HERSHEY_COMPLEX


start = time.time()
fpsf = 0

while True:

   # img,w,h = cam.CaptureRGBA()
    _,img = cam.read()

    h = img.shape[0]
    w = img.shape[1]

    #cvt bc of net.Detect, only used for detections
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA).astype(np.float32)
    frame = ju.cudaFromNumpy(frame)


    dets = net.Detect(frame,w,h)
    # print(dets)
    for d in dets:
        # print(d)
        ID = d.ClassID
        # item = net.GetClassDesc(ID)
        # print(item)
        top = d.Top
        left = d.Left
        bot = d.Bottom
        right = d.Right
        print(top,left,bot,right)
    # disp.RenderOnce(frame,w,h)
    
    dt=time.time()-start
    start = time.time()
    fps=1/dt
    fpsf=.9*fpsf +.1*fps

    text = str(round(fpsf,1))+'fps'
    cv2.putText(img, text, (0,30),font,1,(0,0,255),2)

    cv2.imshow('nanocamsmall',img)
    cv2.moveWindow('nanocamsmall',0,520) 

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
