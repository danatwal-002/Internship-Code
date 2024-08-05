
import face_recognition as fr
import cv2
import os
import pickle

j = 0
names=[]
encodings=[]


with open('train.pkl','rb') as f: #rb: read bytes
    names = pickle.load(f)
    encodings =  pickle.load(f)

im_dir = '/home/sul/Desktop/pyPro/FR_Data/demoImages/unknown'
font = cv2.FONT_HERSHEY_SIMPLEX

for root, dirs, files in os.walk(im_dir):
    for f in files:
        testp = os.path.join(root,f)
        test =  fr.load_image_file(testp)

        facepos = fr.face_locations(test) 
        allencs = fr.face_encodings(test, facepos)

        test = cv2.cvtColor(test, cv2.COLOR_RGB2BGR)

        for (t,r,b,l), fe in zip(facepos, allencs):
            name = 'unknown'
            matches = fr.compare_faces(encodings, fe)
            if True in matches:
                firstmatch = matches.index(True)
                name = names[firstmatch]
            cv2.rectangle(test, (l,t), (r,b),(255,0,0),2)
            cv2.putText(test, name, (l,t-6),font, .75, (255,255,0),2)


        cv2.imshow('test', test)
        cv2.moveWindow('test',0,0)

        if cv2.waitKey(0) == ord('q'):
            cv2.destroyAllWindows()


