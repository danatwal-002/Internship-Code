

#save video to memory card

import cv2

dispW=640 
dispH=480
flip=4 

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet)
x,y = 10,270
bw = int(dispW*0.15)
bh = int(dispH*0.25)
dx,dy= 2,2

while cam.isOpened():

    ret, frame = cam.read()

    cv2.moveWindow('picam',0,0)
    frame = cv2.rectangle(frame, (x,y), (x+bw,y+bh),(255,0,0),-1) #draw rectangle on
    cv2.imshow('picam', frame)   
    x=x+dx
    y=y+dy

    if x <= 0 or x+bw >= dispW:
        dx=dx*(-1)

    if y <=0 or y+bh > dispH:
        dy=dy*(-1)

    if cv2.waitKey(100) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

