
'''
Running funcs at same time (in parallel): threading

bigBox()  #will never acess smallB like this
smallB()

daemon: useful for tasks that need to run continuously in background, are terminated when
main program exits. Non-daemon threads require manual handling to terminate.

Following code ends unless have inf while loop: [they end when program terminates, if we have an
inf loop with no exit statement then program did not finish, therefore daemon thread too not 
finished]

        bbthread.daemon=True
        sbthread.daemon=True

Following code never ends unless forced: [because the threads are associated with funcs that
have inf while loop, if thread is non-daemon then termination is done manually/by force.]

        bbthread.daemon=False
        sbthread.daemon=False

**Useful for when we have 2 cameras running seq & want them to run in parallel.**

'''

import face_recognition as fr
import cv2
import os
import pickle
import time 
from threading import Thread


def bigBox(col):
    while True:
        print(col ,'bigBox opened')
        time.sleep(5) #sleep 5 seconds
        print(col ,'bigBox closed')
        time.sleep(5)

def smallB(col):
    while True:
        print(col ,'smallB opened')
        time.sleep(1)
        print(col ,'smallB closed')
        time.sleep(1)

#create threads
c, c1 = 'red', 'blue'
bbthread = Thread(target=bigBox, args=(c,)) #arg=() for func arguements but my func doesnt have
sbthread = Thread(target=smallB, args=(c1,)) #put comma otherwise wont work

# bbthread.daemon=True
# sbthread.daemon=True

#start threads
bbthread.start()
sbthread.start()

# while True:
#     pass
