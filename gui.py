from tkinter import *
from motorcontrol import *
from time import sleep
from tkinter import filedialog
from threading import Thread
from  simulator import *
from tkinter import messagebox
from sender import *
import serial.tools.list_ports



def getSlider1(val):
        moveX(int(val))
        
   
def getSlider2(val):
        moveY(int(val))

def getSlider3(val):
        moveZ(int(val))    


def select():
    filetypes = (('gcode files', '*.gcode'),)
    global filename
    
    filename = filedialog.askopenfilename(title='OPEN FILE',initialdir='/',filetypes=filetypes)
    print(filename)
    fileName.delete('1.0',END)
    fileName.insert(END, filename)
    

def run():
    screen(filename)

def plott():
    gCode(filename)
    reset()

def Zero():
    sendData(str(5))
    sendData(str(6))
    print('RESET')

def stopper():
    stop()
    

def usbConnection():
    connection()

    
if __name__=='__main__': 

   
    filename = " "
    

    root = Tk()
    root.title('CONTROL PANEL')
    root.resizable(0, 0)

    slider1 = Scale(root, label="X-AXIS", from_=-10, to=10, length=400, activebackground="red", command = getSlider1, orient="horizontal").grid(row=1,column=0,padx= 40, pady= 5)
    slider2 = Scale(root, label="Y-AXIS", from_=-10, to=10, length=400, activebackground="red", command = getSlider2, orient="horizontal").grid(row=2,column=0,padx= 40, pady= 5)
    slider3 = Scale(root, label="Z-AXIS", from_=0, to=1, length=400, activebackground="red", command = getSlider3, orient="horizontal").grid(row=3,column=0,padx= 40, pady= 5)
    

    fileName = Text(root, height = 5, width = 50)
    fileName.grid(row = 1, column = 2,padx= 40, pady= 5, sticky = N)
    selectButton = Button(root, text="SELECT FILE", command=select, width=10).grid(row=2, column=2,padx= 40, pady= 5,sticky = N)
    simButton = Button(root, text="RUN SIMILATION", command=run, width=10).grid(row=3, column=2,padx= 40, pady= 5,sticky = N)
    restartButton = Button(root, text="PLOTT", command=plott, width=10).grid(row=4, column=2,padx= 40, pady= 5,sticky = N)

    

    stopButton = Button(root, text="STOP", command=stopper, width=10).grid(row=2, column=1,padx= 40, pady= 5,sticky = N)
    setButton = Button(root, text="SET 0,0", command=Zero, width=10).grid(row=3, column=1,padx= 40, pady= 5,sticky = N)

    menubar = Menu(root)
    root.config(menu = menubar)
  

    connectionmenu = Menu(menubar)
    menubar.add_cascade(label="connection", menu=connectionmenu)
    connectionmenu.add_cascade(label="usb-ports", command=usbConnection)


    root.mainloop()
