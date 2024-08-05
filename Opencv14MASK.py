
''' Putting OpenCV image on top of live video '''

import cv2

dispW=340
dispH=240
flip=4

img = cv2.imread(r'/home/sul/Downloads/cv.jpg')
img = cv2.resize(img, (340,240))

Grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('img', Grayimg)
# cv2.moveWindow('img', 0,350) 

_, bgmask = cv2.threshold(Grayimg, 225, 255, cv2.THRESH_BINARY)

fgmask = cv2.bitwise_not(bgmask)

# cv2.imshow('fimg', fgmask)
# cv2.moveWindow('fimg', 240,240) 

fg = cv2.bitwise_and(img, img, mask=fgmask)

# cv2.imshow('fg', fg)
# cv2.moveWindow('fg', 240,240) 

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

while True:

    ret, frame = cam.read()
    
    # bg = cv2.bitwise_or(frame, frame, mask=bgmask)
    bg2 = cv2.bitwise_and(frame, frame, mask=bgmask)

    compI = cv2.add(bg2,fg)

    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0)

    # cv2.imshow('bg', bg)
    # cv2.moveWindow('bg',0,350)

    # cv2.imshow('bg2', bg2)
    # cv2.moveWindow('bg2',400,350)

    cv2.imshow('ofg', compI)
    cv2.moveWindow('ofg', 240,240) 


    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()