
import jetson_inference as ji
import jetson_utils as ju
import time
import cv2
import numpy as np

'''

Train our own DNN (training existing networks on objects of interest) --> retraining is 
called Transfer Learning.

Need swap space: bc transfer learning needs extra space

To capture pictures yourself and train on them write in terminal: 
`camera-capture --width=800 --height=600`

'''

net = ji.imageNet('alexnet',['--model=/home/sul/Downloads/jetson-inference/python/training/classification/myModel/resnet18.onnx', '--input_blob=input_0', '--output_blob=output_0', '--labels=/home/sul/Downloads/jetson-inference/myTrain/labels.txt'])
#it's not going to use alexnet, also dont use ~

width = 800
height = 600
dispW = width
dispH = height
flip=2

camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.2 saturation=1.2 ! appsink drop=true'
cam1 = cv2.VideoCapture(camSet)

font = cv2.FONT_HERSHEY_COMPLEX
timeM = time.time()
fpsf=0

while True:
    
    _, frame = cam1.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA).astype(np.float32)
    img = ju.cudaFromNumpy(img)
 
    classID, conf = net.Classify(img,width,height)
    item = ''
    item = net.GetClassDesc(classID)

    dt = time.time() - timeM 
    fps = 1/dt
    fpsf = .95*fpsf + .05*fps
    timeM = time.time()
   
    cv2.putText(frame, str(round(fpsf,1))+' fps '+ item, (0,30), font, 1, (0,0,255),2)
    cv2.imshow('wind',frame)

    cv2.moveWindow('wind',0,0) 

    if cv2.waitKey(1)==ord('q'):
        break

cam1.release()
cv2.destroyAllWindows()