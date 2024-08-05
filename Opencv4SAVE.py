
#save video to memory card

import cv2

# dispW=640 
# dispH=480
# flip=4 

# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

# cam = cv2.VideoCapture(camSet)
# outpvid = cv2.VideoWriter('videos/myCam.avi', cv2.VideoWriter_fourcc(*'XVID'),21,(dispW,dispH))
##XVID is a video codec, needed for writing videos, specified by the fourcc parameter.

# #while True: OR
# while cam.isOpened():

#     ret, frame = cam.read() 
#     cv2.imshow('picam', frame)
#     cv2.moveWindow('picam',0,0)
    
#     outpvid.write(frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cam.release()
# outpvid.release()
# cv2.destroyAllWindows()




###read video from videos folder, comment above code

vid = cv2.VideoCapture('videos/myCam.avi')

while True:

    ret, frame = vid.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(50) == ord('q'):  #50 to slow down
        break

vid.release()        
cv2.destroyAllWindows()