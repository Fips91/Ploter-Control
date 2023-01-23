import serial
import time
import datetime
from tkinter import filedialog
from tkinter import messagebox
import serial.tools.list_ports
from tkinter import *



Port = ''


def sendData(position):
        ser = serial.Serial(port=Port, baudrate = 115200, timeout=0.01)
        
                
        ser.write(position.encode('utf-8'))

        #print(position)
        

def connection():

    def connect():
        global Port
        for i in box.curselection():
            Port = box.get(i)
            Port = Port.split(' ')[0]
            print(Port)
            root.destroy()
            
            

    ports = serial.tools.list_ports.comports()
    
    
    root = Tk()
    root.title('PORTS')

    box = Listbox(root,width=50)
    box.insert(END, *ports)
    box.grid(row=0, column=0,padx= 20, pady= 5)
   
        
    saveButton = Button(root, text="CONNECT", command=connect, width=10).grid(row=2, column=0,padx= 40, pady= 5,sticky = N)

    root.mainloop()

       
