
import cv2

def nth():
    pass

dispW=640
dispH=480
flip=4

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

cv2.namedWindow('nanocam')
cv2.createTrackbar('track','nanocam',0,dispW, nth) #callback func called nothing.
cv2.createTrackbar('track2','nanocam',0,dispH, nth) #callback func called nothing.
cv2.createTrackbar('wid','nanocam',25,dispW, nth) #callback func called nothing.
cv2.createTrackbar('hei','nanocam',25,dispH, nth) #callback func called nothing.

while True:

    ret, frame = cam.read()
    xv = cv2.getTrackbarPos('track','nanocam')
    yv = cv2.getTrackbarPos('track2','nanocam')
    w = cv2.getTrackbarPos('wid','nanocam')
    h = cv2.getTrackbarPos('hei','nanocam')
    cv2.rectangle(frame, (xv,yv), (xv+w,yv+h), (255,0,0),4)

    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0) #move camera to upper left corner

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()