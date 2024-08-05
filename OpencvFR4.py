
'''
FR on all images in db.

Prob with previous code on FR on all images: takes long time to train on small # of imgs.
Sol: train one time & save  training data & load the trained instead of training 
every time.

Pickling: cvt (serialize) objs to byte stream to be saved to a file without worrying about 
internal formatting.

'''

import face_recognition as fr
import cv2
import os
import pickle


encodings = [] #for all unknown in it
names = []
j = 0

im_dir = '/home/sul/Desktop/pyPro/FR_Data/demoImages/known'

#training
for root, dirs, files in os.walk(im_dir):
    for i in files:
        path = os.path.join(root,i) #root is im_dir
        # print(path)
        name = os.path.splitext(i)[0]
        # print(name)

        person = fr.load_image_file(path)
        encoding = fr.face_encodings(person)[0]

        encodings.append(encoding)
        names.append(name)
#end of training

with open('train.pkl','wb') as f:  #wb: write bytes
    pickle.dump(names, f) 
    pickle.dump(encodings, f)


names=[]
encodings=[]

#read 
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
