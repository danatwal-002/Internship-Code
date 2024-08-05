
## mouse callback on left button down
import cv2
import numpy as np
# pt = (-1,-1)
# evt = -1

# def click(event,x,y,flags,params):  #event:scroll, left mouse clikc, right...etc
#     global pt 
#     global evt
#     if event == cv2.EVENT_LBUTTONDOWN:

#         pt = (x,y)
#         evt = event
        

# dispW=640 
# dispH=480
# flip=4 #in new version, for non-flipped image

# cv2.namedWindow('cam') #def window before referencing in moveWindow()
# cv2.setMouseCallback('cam',click) #listener is set up, any time mouse event is detected it calls click()

# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

# cam = cv2.VideoCapture(camSet)

# while cam.isOpened():

#     ret, frame = cam.read() 

#     if evt == 1: #val of cv2.EVENT_LBUTTONDOWN

#         cv2.circle(frame, pt, 8, (0,0,255),-1)
#         fnt = cv2.FONT_HERSHEY_PLAIN
#         xx = str(pt)  #it needs to be string
#         cv2.putText(frame, xx, pt, fnt, 2,(255,0,0),2)

#     cv2.imshow('cam', frame)
#     cv2.moveWindow('cam',0,0)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cam.release()
# cv2.destroyAllWindows()


'''for printing a lot of mouse events at same time, comment above code'''

# coord = [] #global even in funcs
# pt = (-1,-1)
# evt = -1

# def click(event,x,y,flags,params):  #event:scroll, left mouse clikc, right...etc
#     global pt 
#     global evt
#     if event == cv2.EVENT_LBUTTONDOWN:
#         pt = (x,y)
#         coord.append(pt)
#         evt = event
        

# dispW=640 
# dispH=480
# flip=4 #in new version, for non-flipped image

# cv2.namedWindow('cam') #def window before referencing in moveWindow()
# cv2.setMouseCallback('cam',click) #listener is set up, any time mouse event is detected it calls click()

# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

# cam = cv2.VideoCapture(camSet)

# while cam.isOpened():

#     ret, frame = cam.read() 

#     for i in coord:
#         cv2.circle(frame, i, 8, (255,0,0),-1)
#         fnt = cv2.FONT_HERSHEY_PLAIN
#         xx = str(i)  
#         cv2.putText(frame, xx, i, fnt, 1,(255,0,0),2)


#     cv2.imshow('cam', frame)
#     cv2.moveWindow('cam',0,0)

#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

#     if key == ord('c'):
#         coord=[]    

# cam.release()
# cv2.destroyAllWindows()


'''get RGB Vals with right mouse click and keep left mouse click as well:'''

coord = [] #global even in funcs
pt = (-1,-1)
evt = -1
colors = np.zeros((250,250,3), np.uint8)

def click(event,x,y,flags,params):  #event:scroll, left mouse clikc, right...etc

    global pt 
    global evt

    if event == cv2.EVENT_LBUTTONDOWN:

        pt = (x,y)
        coord.append(pt)
        evt = event

    if event == cv2.EVENT_RBUTTONDOWN:

        blue = frame[y,x,0]
        green = frame[y,x,1]
        red = frame[y,x,2]
        colstring = str(blue)+','+str(green)+','+str(red)
        colors[:] = [blue, green, red]
        fnt = cv2.FONT_HERSHEY_PLAIN

        r=255-int(red)
        g=255-int(green)
        b=255-int(blue)
        tp=(b,g,r)

        cv2.putText(colors, colstring, (10,25), fnt,1,tp, 2)
        cv2.imshow('image', colors)
        

dispW=640 
dispH=480
flip=4 #in new version, for non-flipped image

cv2.namedWindow('cam') #def window before referencing in moveWindow()
cv2.setMouseCallback('cam',click) #listener is set up, any time mouse event is detected it calls click()

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet)

while cam.isOpened():

    ret, frame = cam.read() 

    for i in coord:
        cv2.circle(frame, i, 8, (255,0,0),-1)
        fnt = cv2.FONT_HERSHEY_PLAIN
        xx = str(i)  
        cv2.putText(frame, xx, i, fnt, 1,(255,0,0),2)
        
 
    cv2.imshow('cam', frame)
    cv2.moveWindow('cam',0,0)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    if key == ord('c'):
        coord=[]    

cam.release()
cv2.destroyAllWindows()
