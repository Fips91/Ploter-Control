from sender import *
from time import sleep
from tkinter import messagebox
import sys
import threading

stopThread = False


def moveX(val):
    
    if val == 0:
        sendData(str(0))
        
    elif val > 0:
        sendData(str(1))
      
    elif val < 0:
        sendData(str(2))


def moveY(val):
    
    if val == 0:
        sendData(str(0))
       

    elif val > 0:
        sendData(str(3))
        
    elif val < 0:
        sendData(str(4))

def moveZ(val):
    
    if val == 1:
        sendData(str(6))
        
        
    elif val == 0:
        sendData(str(7))

def stop():
    global stopThread
    stopThread = True
    sendData(str(0))
    print('STOP')


def gCode(filename):
    global stopThread
    stopThread = False

    def process(filename):
        global stopThraed

        file = open(filename)
        
        for line in file:
            sendData(line)
            print(line)
            print()
            if stopThread == True:
                break
            #sleep(0.1)
            
           
                    
        sendData(str(5))
        sendData(str(6))

    thread = threading.Thread(target = process, args = (filename,))
    thread.start()
    
