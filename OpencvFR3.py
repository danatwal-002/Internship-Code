
import face_recognition as fr
import cv2
import os


'''
FR on all images in db in simpler way, compare to one unknown img only*:

Instead of loading each image one by one, use `os.walk('path to folder of images to load')` for
generating all the files & directories' names in a directory tree, output --> root, directories,
files, files: A list of files in the current directory (string), then we join the file name to
the root to create the full path to the file.

'''

# encodings = [] #for all unknown in it
# names = []
# j = 0

# #training

# im_dir = '/home/sul/Desktop/pyPro/FR_Data/demoImages/known'

# for root, dirs, files in os.walk(im_dir): 

#   # print(files)
#    for i in files:
#         print(i)
#         path = os.path.join(root,i) 
#         print(path)
#         name = os.path.splitext(i)[0]
#         # print(name)

#         person = fr.load_image_file(path)
#         encoding = fr.face_encodings(person)[0]

#         encodings.append(encoding)
#         names.append(name)
# #end of training

# print(names)        

# font = cv2.FONT_HERSHEY_SIMPLEX

# test = fr.load_image_file('/home/sul/Desktop/pyPro/FR_Data/demoImages/unknown/u4.jpg')
# facepos = fr.face_locations(test)
# allenc = fr.face_encodings(test, facepos)

# test = cv2.cvtColor(test, cv2.COLOR_RGB2BGR)

# for (t,r,b,l), fe in zip(facepos, allenc):
#     name = 'unknown'
#     matches = fr.compare_faces(encodings, fe)
#     if True in matches:
#         firstmatch = matches.index(True)
#         name = names[firstmatch]
#     cv2.rectangle(test, (l,t), (r,b),(255,0,0),2)
#     cv2.putText(test, name, (l,t-6),font, .75, (255,255,0),2)


# cv2.imshow('test', test)
# cv2.moveWindow('test',0,0)

# if cv2.waitKey(0) == ord('q'):
#     cv2.destroyAllWindows()


''' 
*FR on all images in db, compare to many unknown imgs*

'''


encodings = [] 
names = []
j = 0

im_dir = '/home/sul/Desktop/pyPro/FR_Data/demoImages/known'

for root, dirs, files in os.walk(im_dir):
    for i in files:
        path = os.path.join(root,i) #root is im_dir
        name = os.path.splitext(i)[0]

        person = fr.load_image_file(path)
        encoding = fr.face_encodings(person)[0]

        encodings.append(encoding)
        names.append(name)


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
            matches = fr.compare_faces(encodings, fe) #compare each img in known db to each img in unknown folder
            if True in matches: #if match then draw a box/write text on that unknown img
                firstmatch = matches.index(True)
                name = names[firstmatch]
            cv2.rectangle(test, (l,t), (r,b),(255,0,0),2)
            cv2.putText(test, name, (l,t-6),font, .75, (255,255,0),2)


        cv2.imshow('test', test)
        cv2.moveWindow('test',0,0)

        if cv2.waitKey(0) == ord('q'):
            cv2.destroyAllWindows()
