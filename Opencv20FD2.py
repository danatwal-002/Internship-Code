

'''
Get pre-trained model (Haar Cascade Classifier) to detect eyes.

'''

import cv2

dispW=640
dispH=480
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)
 
eye_casc = cv2.CascadeClassifier(r'/home/sul/Desktop/pyPro/cascade/eye.xml')
face_casc = cv2.CascadeClassifier(r'/home/sul/Desktop/pyPro/cascade/face.xml')

while True:

    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #find the eye inside face
    faces = face_casc.detectMultiScale(gray,1.3,8)

    for (x,y,w,h) in faces:

        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)

        roi_g = gray[y:y+h, x:x+w] #for detecting eyes in face region
        roi_c = frame[y:y+h, x:x+w] #for drawing

        eyes = eye_casc.detectMultiScale(roi_g)

        for (xi,yi,wi,hi) in eyes:
            cv2.circle(roi_c, (int(xi+wi/2), int(yi+hi/2)), 16, (255,255,0),2)

    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,700)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
