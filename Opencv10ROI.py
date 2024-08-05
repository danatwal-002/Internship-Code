
import cv2

dispW=640
dispH=480
flip=4

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)
 
while True:

    ret, frame = cam.read()

    roi = frame[50:200, 200:400] #referencing back to same img, if img changes this would too
    sepROI = frame[50:200, 200:400].copy() #does not reference back to old img
    grayroi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    grayROI2 = cv2.cvtColor(grayroi, cv2.COLOR_GRAY2BGR)
    # frame[50:200, 200:400] = [255,255,255] #make spot white
    frame[50:200, 200:400] = grayROI2 #make spot white
 
    cv2.imshow('roi', roi)
    cv2.moveWindow('roi',0,720)

    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0) 
    
    cv2.imshow('grayroi',grayroi)
    cv2.moveWindow('grayroi',200,200) 
    
    cv2.imshow('seproi',sepROI)
    cv2.moveWindow('seproi',300,600) 


    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()