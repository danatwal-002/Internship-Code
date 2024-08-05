
'''
FR on live cam.
[Show image, and let it recognize who, image has to be face of
person in known db that it was trained on]

fr.face_locations() --> inp: image, model (opt) for FR
        model is by def HOG, we used cnn which is more accurate but slower than HOG 
        for finding faces, but bc we have many processors on Jetson Nano we use cnn
        bc we can do this in parallel (adv of Jetson Nano) -> best FR model (cnn) which 
        usually runs slower but on JN runs fast. 

Downsampling the frames by factor of 3 for better speed, but since the calculation of the coords
of the face was done on the downsampled frames, and we draw the rectangle on the normal live 
frames then we have to multiply the coords by 3 for drawing/mapping accurately.

*Many real-time face recognition applications prioritize speed, as they need to process frames 
in near real-time. Downsampling helps achieve this goal by reducing the computational load.

Trade off: the more we scale down an image, the faster it will be,
but the face it has to recognize gets bigger, so has to be closer to camera

'''

import face_recognition as fr
import cv2
import os
import pickle

encs = []
names = []

#reading the file that has training data saved in
with open('train.pkl', 'rb') as f: 
    names = pickle.load(f)
    encs = pickle.load(f)

# dispW=640
# dispH=480
flip=2

# faster but need pic very close:
dispW=320
dispH=240

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

fnt = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = cam.read() #reads in BGR, but FR software operates in RGB 
    frameS = cv2.resize(frame, (0,0), fx=.33, fy=.33) #scaling down by factor of 3 (downsampling)

    frameRGB = cv2.cvtColor(frameS, cv2.COLOR_BGR2RGB)

    facepos = fr.face_locations(frameRGB, model='cnn') 
    allencs = fr.face_encodings(frameRGB, facepos)  #num of encs == num of faces

    for (t,r,b,l),face_enc in zip(facepos, allencs):
        name = 'unknown person'
        matches = fr.compare_faces(encs,face_enc) #compare known imgs to frames on live video
        
        if True in matches:
            indx = matches.index(True)
            name = names[indx]
        
        t=t*3
        b=b*3
        r=r*3
        l=l*3
        cv2.rectangle(frame, (l,t), (r,b), (255,0,0),2)    
        cv2.putText(frame, name, (l,t-6), fnt,.75, (0,0,255),2)
        

    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0) #move camera to upper left corner

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
    