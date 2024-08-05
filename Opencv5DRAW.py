
#save video to memory card

import cv2

dispW=640 
dispH=480
flip=4 

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet)

while cam.isOpened():

    ret, frame = cam.read()
    frame = cv2.rectangle(frame, (200,20), (100,150),(255,0,0),-1) #draw rectangle on
    # frame = cv2.circle(frame,(320,240),50,(255,0,0),4) #draw circle in middle, 50 is radius
    ## for full shape, instead of 4 put -1

    # fnt = cv2.FONT_HERSHEY_DUPLEX   #define font
    # frame = cv2.putText(frame, 'first text here',(300,300),fnt, 1,(255,150,0),2) #1 is size of letters
    
    # frame = cv2.line(frame, (100,50), (630,470), (0,0,255),4)
    cv2.imshow('picam', frame)
    cv2.moveWindow('picam',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

