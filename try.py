
import cv2
import numpy as np

colors = np.zeros((250,250,3), np.uint8)

def click(event, x, y, flags, params):

    if event == cv2.EVENT_RBUTTONDOWN:

        r = frame[y,x,0]
        g = frame[y,x,1]
        b = frame[y,x,2]

        colors[:] = [r,g,b]
        colstr = str(r)+','+str(g)+','+str(b)
        fnt = cv2.FONT_HERSHEY_DUPLEX   #define font
        cv2.putText(colors, colstr, (30,30), fnt,1,(255,150,0),1)
        cv2.imshow('cols', colors)


dispW=640
dispH=480
flip=4

cv2.namedWindow('win')
cv2.setMouseCallback('win',click)

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

while True:

    ret, frame = cam.read()

    cv2.imshow('win',frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


