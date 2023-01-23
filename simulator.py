import turtle
from turtle import *
from tkinter import filedialog
from time import sleep
from tkinter import messagebox
import sys
from motorcontrol import *


filename = ''
Koordinates = [0, 0, 0]
prevKoord = [0, 0, 0]
row = 0



def reset():
    global Koordinates
    global prevKoord
    Koordinates = [0, 0, 0]
    prevKoord = [0, 0, 0]


def screen(filename):

    global Koordinates
    global prevKoord
    global time
    global row
   

    turtle.TurtleScreen._RUNNING=True
    window=turtle.Screen()
    window.setup(450,450)
    window.bgcolor('grey')
    window.title("SIMULATION")
    pen = turtle.Turtle()
    pen.pensize(4)
    
    



    file = open(filename)
    pen.up()
    
    for line in file:
        
                
                
                        
        if line.find('X')!=-1:
            posX =line.index("X")
            if float(line[posX+1:posX+7]) != Koordinates[0]:
                prevKoord[0] = Koordinates[0]
                Koordinates[0] = float(line[posX+1:posX+7])
                                    

        if line.find('Y')!=-1:
            posY =line.index("Y")
            if float(line[posY+1:posY+7]) != Koordinates[1]:
                prevKoord[1] = Koordinates[1]
                Koordinates[1] = float(line[posY+1:posY+7])
                                    

        if line.find('Z')!=-1:
            posZ =line.index("Z")
            if float(line[posZ+1:posZ+5]) != Koordinates[2]:
                prevKoord[2] = Koordinates[2]
                Koordinates[2] = float(line[posZ+1:posZ+5])

            
        print()
        print(prevKoord)
        print(Koordinates)

        if Koordinates[2] < 0:
            pen.down()

        if Koordinates[2] > 0:
            pen.up()
            

        pen.goto(Koordinates[0]-200, Koordinates[1]+200)
  
        
                                
    pen.up()
    reset()
    turtle.done
    window.exitonclick()
