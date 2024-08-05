
import cv2

dispW=640
dispH=480
flip=4

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

x,y = 0,0
w = int(dispW*0.26)
h = int(dispH*0.26)
d,d2 = 2,2

while True:

    ret, frame = cam.read()
   
    roi = frame[y:y+h, x:x+w].copy()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    
    frame[y:y+h, x:x+w] = roi
    frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
   
    x = x+d
    y =  y+d2

    if x == 0 or x+w == dispW:
        d=d*(-1)

    if y == 0 or y+h == dispH:
        d2=d2*(-1)     

    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0) 

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()