
import face_recognition as fr
import cv2
import os
import pickle
import time 

'''
See how many  FPS we have & how can we optimize

'''

fpsR = 0
sf = 0.10

#see present time
timeStamp = time.time()


encs = []
names = []
with open('train.pkl', 'rb') as f: 
    names = pickle.load(f)
    encs = pickle.load(f)

dispW=640
dispH=480
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

fnt = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = cam.read() #reads in BGR, but FR software operates in RGB 
    frameS = cv2.resize(frame, (0,0), fx=sf, fy=sf) 

    frameRGB = cv2.cvtColor(frameS, cv2.COLOR_BGR2RGB)

    facepos = fr.face_locations(frameRGB, model='cnn') 
    allencs = fr.face_encodings(frameRGB, facepos)  #num of encs == num of faces

    for (t,r,b,l),face_enc in zip(facepos, allencs):
        name = 'unknown person'
        matches = fr.compare_faces(encs,face_enc)

        if True in matches:
            indx = matches.index(True)
            name = names[indx]
        
        t=int(t/sf)
        b=int(b/sf)
        r=int(r/sf)
        l=int(l/sf)
        cv2.rectangle(frame, (l,t), (r,b), (255,0,0),2)    
        cv2.putText(frame, name, (l,t-6), fnt,.75, (0,0,255),2)
        
    dt = time.time() - timeStamp
    fps=1/dt
    fpsR=.85*fpsR + 0.15*fps

   # print('fps: ',round(fpsR,2))
    timeStamp = time.time()

    cv2.rectangle(frame, (0,0), (100,40),(255,255,0),-1)
    cv2.putText(frame, str(round(fpsR,1))+'fps',(0,25), fnt ,.75, (255,0,0),2)
    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0) 
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
    