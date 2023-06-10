from reciver import reciver
from motor import Stepper
from motor import *
from time import sleep_us
from machine import Pin, PWM
import sys



motor1 = Stepper(StepPin = 14, DirPin = 15)
motor2 = Stepper(StepPin = 12, DirPin = 13)
servo = PWM(Pin(11))
servo.freq(50)
reciver1 = reciver(115200)


def main():
    data = ''
    inPut = ''
    xCoor = 0
    yCoor = 0
    zCoor = 0
    


    while True:
        
        inPut = reciver1.reciveData()
        
                
                 
        if inPut == '5':
            reset()
            main()
        
        
        elif inPut == '6':
            servo.duty_u16(5800)   #servo up
            sleep_us(10000)
                
                  
                        
        elif inPut == '7':
            servo.duty_u16(8200)   #servo down
            sleep_us(10000)
                
                   
        
        
        
        elif inPut in ['0', '1', '2', '3', '4']:
            data = inPut
            #print(data)
                  
            
        elif data == '1':
            xMotion(motor1,motor2,1)   #x right
                
                    
        elif data == '2':
            xMotion(motor1,motor2,0)   #x left
              
                        
        elif data == '3':
            yMotion(motor1,motor2,1)   #y up
                
                    
        elif data == '4':
            yMotion(motor1,motor2,0)   #y down
       
            
                
        elif inPut != None:
           
            #print(inPut)
            #inPut = inPut.strip('\n')
            #inPut = inPut.strip('G1')
            commands = inPut.split()
            
            for x in commands:
                
                if x.find('X')!=-1:
                    
                    posX = x.index("X")
                    xCoor = x[posX+1:]
                        
                                  

                if x.find('Y')!=-1:
                    
                    posY =x.index("Y")
                    yCoor = x[posY+1:]
                        
                        

                if x.find('Z')!=-1:
                   
                    posZ = x.index("Z")
                    zCoor = x[posZ+1:]
                        
                        
            try:
                z = float(zCoor)
                
            except Exception as e:
                print(e)
                print()
                
                
                
            if z >= 0:
                    servo.duty_u16(5800)   #servo up
                    sleep_us(10000)
                   
                    
            elif z < 0:
                servo.duty_u16(8200)   #servo down
                sleep_us(10000)
                    
           
              
            MoveTo(xCoor, yCoor,motor1,motor2)
                    
            #sleep_us(1000)
                                
            
                 
          
    
 
if __name__ == "__main__":
    main()
    
    
