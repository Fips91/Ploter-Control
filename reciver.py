import utime
import machine
from utime import sleep



class reciver:
    
    def __init__(self, baund):
    
        self.uart = machine.UART(0, baudrate = int(baund),)
        
        self.recive = None
    
    

    def reciveData(self):
        
        
        if self.uart.any():
            
           
            
            self.recive = self.uart.readline()
            
            data = self.recive.decode('utf-8')
            #print(type(data))
            #print(data)
            
            return data
            
            
