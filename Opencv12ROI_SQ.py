

import cv2

flag = 0 

def click(event, x, y, flags, params):
    global x1,y1,x2,y2
    global flag

    if event == cv2.EVENT_LBUTTONDOWN:
        flag=0
        x1=x
        y1=y
      
    if event == cv2.EVENT_LBUTTONUP:
        flag=1
        x2=x
        y2=y

        
        
dispW=640
dispH=480
flip=4
# bw = int(dispW*2)
# bh = int(dispH*2)

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

cv2.namedWindow('cam')
cv2.setMouseCallback('cam', click)
while True:

    ret, frame = cam.read()
    cv2.imshow('cam',frame)

    if flag == 1:
        cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,255), 3)
        roi = frame[y1:y2, x1:x2].copy()
        cv2.imshow('roi',roi)
        cv2.moveWindow('roi',800,0)

    cv2.moveWindow('cam',0,0)    

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()