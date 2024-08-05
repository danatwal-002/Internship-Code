
import face_recognition as fr
import cv2
import os
import pickle



encodings = [] 
names = []

im_dir = '/home/sul/Desktop/pyPro/FR_Data/demoImages/known'

for root, dirs, files in os.walk(im_dir):
    for i in files:
        path = os.path.join(root,i) 
        print(path)
        name = os.path.splitext(i)[0]
        print(name)

        person = fr.load_image_file(path)
        encoding = fr.face_encodings(person)[0]

        encodings.append(encoding)
        names.append(name)


with open('train.pkl','wb') as f:  #wb: write bytes
    pickle.dump(names, f) 
    pickle.dump(encodings, f)
