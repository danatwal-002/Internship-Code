
'''

Overview of face_recognition Library:

  -FR using face_recognition library, the code detects faces, doesn't actually perform FR 
  i.e. identifying known individuals, here we focused on the face detection aspect 
  to locate positions of faces in the loaded image, it doesn't involve comparison with known 
  faces/databases.


Difference between FD and FR:

  -Face Detection: locating and identifying faces in an image or video. It doesn't 
  identify who the individuals are; only tells you where their faces are.

  -Face Recognition: Goes a step further by identifying who the person is based on their 
  facial features by comparing the detected face with a db of known faces to determine if 
  there's a match. 




Why use `load_image_file()` from the face_recognition library, and not load the
image using OpenCV for example?
  *It's possible to do either, but `load_image_file()` from fr handles all image loading and 
  optimization specifically for face recognition tasks, it takes care of any necessary 
  preprocessing steps to prepare the image for face detection and recognition. This includes 
  things like color space conversions, resizing, ...etc.
  
  *OpenCV reads images in the BGR color space, face_recognition expects images in RGB color 
  space so using OpenCV means converting to RGB for fr, and back to BGR for OpenCV which we
  don't have to do using `load_image_file()` since it takes care of the necessary image 
  preprocessing for FR tasks, this makes code cleaner and more focused on the specific task.


To detect faces use face_locations() which returns coords of the faces it finds
(top,right,bottom,left)


'''


import face_recognition as fr
import cv2

#load image using face_recognition:
img = fr.load_image_file(r'/home/sul/Desktop/pyPro/FR_Data/demoImages/unknown/u3.jpg')

#load image using OpenCV:
img = cv2.imread(r'/home/sul/Desktop/pyPro/FR_Data/demoImages/unknown/u3.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


face_loc = fr.face_locations(img)
print(face_loc)  #found 2 faces, 2 arrs of tuples of coords of the faces found

#FR uses RGB, opencv uses BGR 
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

#draw box around faces:
for (top,right,bottom,left) in face_loc:
    cv2.rectangle(img, (right,top), (left,bottom), (255,0,0), 2)
    

cv2.imshow('window', img)
cv2.moveWindow('window',0,0)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()

