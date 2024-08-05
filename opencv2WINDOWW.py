
import cv2
print(cv2.__version__)

dispW=640
dispH=480
flip=4

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)

while True:

    ret, frame = cam.read()
    
    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0) #move camera to upper left corner

    cv2.imshow('nanocam2',frame)
    cv2.moveWindow('nanocam2',700,0) #move camera to upper left corner

    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    

    cv2.imshow('gcam',gray)
    cv2.moveWindow('gcam',0,520) #move camera underneath it

    cv2.imshow('gcam2',gray)
    cv2.moveWindow('gcam2',700,520) #move camera to upper left corner

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()