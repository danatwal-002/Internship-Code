
'''

Face Detection: Get pre-trained model (Haar Cascade classifier) for FD.
    -Download from GitHub into a folder called cascade, then load it as face_casc.


cv2.CascadeClassifier(path): class that represents pre-trained cascade classifier for obj 
detection, it includes Haar CC. Classifier is loaded from the XML file located at 
the given path. So face_casc is an instance of class CascadeClassifier, the class' methods
can be used through face_casc.

face.xml --> pre-trained face cascade classifier. 

face_casc.detectMultiScale(image, scaleFactor, minNeighbours): for detecting faces in grayscale
    frame using Haar CC, returned faces will be list of arrs, each will have x,y,w,h of box.

    -scaleFactor --> how much the image size is reduced at each image scale, smaller 
    value will increase detection accuracy (finer scale search) but reduce speed.
    -minNeighbours --> # of overlapping rectangles to be grouped together to be considered a 
    valid detection. For example, if this parameter is set to 3, it means that for a region in 
    the image to be considered a valid detection, there must be at least 3 overlapping bounding 
    boxes around that region. 
        - This helps reduce false positives. 
        - Higher value means less detections with high quality.
        - Acts as a form of Non-Maximum Suppression.  It doesn't rely on confidence scores like 
        NMS but instead counts # of overlapping neighbors.



Haar Cascade classifiers are effective for detecting simple objects or features with distinct 
patterns, such as faces, eyes, and cars, in real-time. It can detect muliple objects in an img.
    
The "cascade" in Haar Cascade classifier refers to the way it is organized into multiple stages,
where each stage contains a subset of patterns [defined by Haar-like features] that classifier
has been trained on.


Haar-like features are rectangular filters that capture basic patterns of contrast 
and brightness variations in images. By evaluating these features across different regions 
of an image, the classifier can determine whether certain object-like patterns are present.
    
'''

import cv2

dispW=640
dispH=480
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)


face_casc = cv2.CascadeClassifier(r'/home/sul/Desktop/pyPro/cascade/face.xml')

while True:

    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #turn to gray bc in FR it's easier to deal with no color, less computational load
    
    faces = face_casc.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)

    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
