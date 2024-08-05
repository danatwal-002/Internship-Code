
'''
Actual FR code, train on 2 images.

Learning faces: to learn face, have to load face then encode it (in order to compare)

Here we use fr.face_encodings() because we have a db of known faces which we want to
compare to detected faces in unknown img to idenitfy if it recognizes the faces in it, so we 
encode the image and that means converting to a numerical rep that captures distinctive feats.
Encodings are unique to each face.

fr.face_encodings(face_img, known_face_locs=None)
--> inp: face_img should be in RGB format, known_face_locs should be (top, right, bottom, left).
    If known_face_locs is unprovided, function will use face_locations() internally.
--> outp: list of arrs, if we have more than one encoding it returns series of arrs, each reps facial encoding of a detected face in img.

OpenCV uses BGR format while face_recogition library uses RGB format, that is why input image
must be in RGB format.


fr.compare_faces(known_face_encs,face_enc_tocheck, tolerance=0.6)
--> inp: known_face_encs --> from known db, could be a list of known faces' encodings.
    face_enc_tocheck --> unknown, single encoding fo face against known faces to identify it.
    tolerance parameter is optional, specifies tolerance level for face matching.
--> outp: list of bool vals of whether known face encs match unknown fac enc.

'''

import face_recognition as fr
import cv2
from PIL import Image


font = cv2.FONT_HERSHEY_SIMPLEX

#load & encode img
img = fr.load_image_file(r'/home/sul/Desktop/pyPro/FR_Data/demoImages/known/Donald Trump.jpg')
face_loc = fr.face_locations(img)
imgEnc = fr.face_encodings(img)[0] #take first (primary face detected in img)
print(type(imgEnc)) #outp is <class 'numpy.ndarray'>


img2 = fr.load_image_file(r'/home/sul/Desktop/pyPro/FR_Data/demoImages/known/Nancy Pelosi.jpg')
imgEnc2 = fr.face_encodings(img2)[0]  

Encs = [imgEnc, imgEnc2]
names = ['the_donald','the_nancy']

test = fr.load_image_file(r'/home/sul/Desktop/pyPro/FR_Data/demoImages/unknown/u3.jpg')
test_face_pos = fr.face_locations(test)
test_encs = fr.face_encodings(test, test_face_pos)


test = cv2.cvtColor(test, cv2.COLOR_RGB2BGR)

for (r1,c1,r2,c2), face_encoding in zip(test_face_pos, test_encs):
    name = 'unknonw'
    matches = fr.compare_faces(Encs, face_encoding)

    if True in matches:
        first_match_indx = matches.index(True) #get indx of where True occured in list
        name = names[first_match_indx] #get name
    cv2.rectangle(test, (c1,r1), (c2,r2), (255,0,0), 2)
    cv2.putText(test,name, (c1,r1-6), font, .75, (255,0,255),2)



cv2.imshow('test', test)
cv2.moveWindow('test',0,0)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()


