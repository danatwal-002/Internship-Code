
import cv2
import numpy as np

dispW=640
dispH=480
flip=4

img1 = np.zeros((480,640,1), np.uint8)
img2 = np.zeros((480,640,1), np.uint8)

img1[0:480, 0:320] = [255] 
img2[190:290, 270:370] = [255]

bitand = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1, img2)
bitxor = cv2.bitwise_xor(img1, img2)


camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)


while True:

    ret, frame = cam.read()

    frame = cv2.bitwise_and(frame, frame, mask=img2)
    
    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0)

    # cv2.imshow('im1',img1)
    # cv2.moveWindow('im1',500,0)

    # cv2.imshow('im2',img2)
    # cv2.moveWindow('im2',800,500)

    # cv2.imshow('ba',bitand)
    # cv2.moveWindow('ba',800,0)

    # cv2.imshow('bor',bitOr)
    # cv2.moveWindow('bor',340,0)

    # cv2.imshow('bxor',bitxor)
    # cv2.moveWindow('bxor',900,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()