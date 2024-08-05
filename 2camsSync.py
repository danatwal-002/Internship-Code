
from threading import Thread 
import cv2
import numpy as np

'''
 Class vstream to manage a camera:
want it to launch a camera, collect frames, allow user to grab a frame (make them available).
Class will have a thread that will constantly gather frames. Launching camera should only
be done one time, so should be done in the init. 

 self.thread = Thread(target=self.update, args=()) --> create thread to contin read frames 
from cam1, we target a method 'update'


'''

class vStream:
    def __init__(self, src,w,h):
        self.w = w
        self.h = h
        self.cap = cv2.VideoCapture(src) #launching cam
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self): #for contin read frames
        while True:
            _, self.frame = self.cap.read() #putting self bc we have multip cams
            self.frame2 = cv2.resize(self.frame, (self.w,self.h)) #resizing

    def getFrame(self):
         return self.frame2       


dispW=640 
dispH=480
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam2 = vStream(camSet,dispW, dispH)
cam1 = vStream(1,dispW,dispH)  

while True:
    try:
        web = cam1.getFrame()
        # cv2.imshow('web',web)

        rpi = cam2.getFrame()
        # cv2.imshow('rpi',rpi)

        myFrame3=np.hstack((web,rpi))

        cv2.imshow('ComboCam',myFrame3)
        cv2.moveWindow('ComboCam',0,0)

    except:    
       print('frames not available')
        #  pass

    if cv2.waitKey(1) == ord('q'):
        cam1.capture.release()
        cam2.capture.release()

        cv2.destroyAllWindows()    
        # exit(1)
        break

