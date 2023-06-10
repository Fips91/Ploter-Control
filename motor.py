from machine import Pin
from time import sleep_us
from reciver import reciver
import sys

xPos = 0
yPos = 0
SLEEP = 100
go = False
    
class Stepper:
    
   
    
    def __init__(self, StepPin, DirPin):
        self.step = Pin(StepPin, Pin.OUT)
        self.dir = Pin(DirPin, Pin.OUT)
        
                   
    def rotate(self, Direc):
        global SLEEP
  
        if Direc == 0:
            self.dir.value(0)
            
            self.step.value(1)
            self.step.value(0)
            sleep_us(SLEEP)
            
        
   
        elif Direc == 1:
            self.dir.value(1)
            
            self.step.value(1)
            self.step.value(0)
            sleep_us(SLEEP)
            
            
            

def xMotion(motor1,motor2,direc):
    global xPos
    global yPos
    
    if direc == 1:
        motor1.rotate(1)
        motor2.rotate(1)
        xPos += 1
    
    else:
        motor1.rotate(0)
        motor2.rotate(0)
        xPos -= 1
        
    #print('X '+str(xPos)+' Y '+str(yPos))
        
        
    
def yMotion(motor1,motor2,direc):
    global yPos
    global xPos
    
    if direc == 1:
        motor1.rotate(0)
        motor2.rotate(1)
        yPos -= 1
    
    else:
        motor1.rotate(1)
        motor2.rotate(0)
        yPos += 1
        
    #print('X '+str(xPos)+' Y '+str(yPos))



def reset():
    global xPos
    global yPos
    
    xPos = 0
    yPos = 0
    print('reset')
    
    
    
           
def MoveTo(X, Y, motorRight, motorLeft): #motor1=motorRight, motor2 = motorLeft
    
    global SLEEP
    global xPos
    global yPos
  
    try:
        x = -1*float(X)
        y = float(Y)
        go = True
    except Exception as e:
        go = False
        print(e)
        print()
                
 
            
    if go == True:
        
        x = x*(20011/400)
        y = y*(20146/400)
        xDiff = round(x) - -xPos #how mutch the pen needs to move in x direction
        yDiff = round(y) - yPos #how mutch the pen needs to move in y direction
        
        print('X1 '+str(xPos)+' Y1 '+str(yPos)+'  =>  X2 '+str(x)+' Y2 '+str(y))
        print()
        
        
        
        xDirec = 0 if xDiff > 0 else 1 #witch direction right motor needs to move
        yDirec = 0 if yDiff > 0 else 1 #witch direction left motor needs to move
        
        
        xDiff = abs(xDiff)
        yDiff = abs(yDiff)

       
        if xDiff == yDiff:
            for i in range(xDiff):
                xMotion(motorRight,motorLeft,xDirec)
                yMotion(motorRight,motorLeft,yDirec)
                sleep_us(SLEEP)
            
        else:
            error = 0
            increment = yDiff/xDiff if xDiff > yDiff else xDiff/yDiff
            
            if xDiff > yDiff:
                for i in range(xDiff):
                    xMotion(motorRight,motorLeft,xDirec)
                    error += increment
                    if error >= 1:
                        yMotion(motorRight,motorLeft,yDirec)
                        error -= 1
                    sleep_us(SLEEP)
                
            elif xDiff < yDiff:
                for i in range(yDiff):
                    yMotion(motorRight,motorLeft,yDirec)
                    error += increment
                    if error >= 1:
                        xMotion(motorRight,motorLeft,xDirec)
                        error -= 1
                    sleep_us(SLEEP)
                    
        go = False
                    

    

