from ast import keyword
from tkinter import *
import tkinter.font
from gpiozero import LED
import time
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

win = Tk()
win.title("Morse Code Calculator")
win.geometry("280x170")
myFont = tkinter.font.Font(family = 'Helvetica', size = 10, weight = 'bold')
led = LED(17)
def dot():
    led.on()
	time.sleep(0.3)
    led.off()
	time.sleep(0.3)
    print("Dot")

def dash():
	led.on()
	time.sleep(0.9)
	led.off()
	time.sleep(0.3)
    print("dash")

def close():
    win.destroy()
    
def MorseCode():
    text = Text_Box.get('1.0','end-1c')
    if len(text) > 12 or len(text) < 0:
        led.off()
        print("Text too long")
        print("Max. words allowed") 
        return
    else:
        print("Calculating....")
        time.sleep(1)

    for keyword in text:    
        if keyword.lower() == 'a':
            dot()
            dash()

        elif keyword.lower() == 'b':
            dash()
            dot()
            dot()
            dot()

        elif keyword.lower() == 'c':
            dash()
            dot()
            dash()
            dot()


        elif keyword.lower() == 'd':
            dash()
            dot()
            dot()
            
        elif keyword.lower() == 'e':
            dot()
            
        elif keyword.lower() == 'f':
            dot()
            dot()
            dash()
            dot()
            
        elif keyword.lower() == 'g':
            dash()
            dash()
            dot()

        elif keyword.lower() == 'h':
            dot()
            dot()
            dot()
            dot()
            
        elif keyword.lower() == 'i':
            dot()
            dot()

        elif keyword.lower() == 'j':
            dot()
            dash()
            dash()
            dash()
            
        elif keyword.lower() == 'k':
            dash()
            dot()
            dash()
            
        elif keyword.lower() == 'l':
            dot()
            dash()
            dot()
            dot()
            
        elif keyword.lower() == 'm':
            dash()
            dash()

        elif keyword.lower() == 'n':
            dash()
            dot()
            
        elif keyword.lower() == 'o':
            dash()
            dash()
            dash()
            
        elif keyword.lower() == 'p':
            dot()
            dash()
            dash()
            dot()
            
        elif keyword.lower() == 'q':
            dash()
            dash()
            dot()
            dash()
            
        elif keyword.lower() == 'r':
            dot()
            dash()
            dot()
            
        elif keyword.lower() == 's':
            dot()
            dot()
            dot()
            
        elif keyword.lower() == 't':
            dash()
            
        elif keyword.lower() == 'u':
            dot()
            dot()
            dash()
            
        elif keyword.lower() == 'v':
            dot()
            dot()
            dot()
            dash()
            
        elif keyword.lower() == 'w':
            dot()
            dash()
            dash()
            
        elif keyword.lower() == 'x':
            dash()
            dot()
            dot()
            dash()
            
        elif keyword.lower() == 'y':
            dash()
            dot()
            dash()
            dash()
            
        elif keyword.lower() == 'z':
            dash()
            dash()
            dot()
            dot()

Label(win, text = 'Enter the name', bg = 'bisque2', font = myFont, height = 1, width = 35).grid(row = 0, column = 1)

Text_Box = Text(win, height = 1, width = 30, bg = 'grey')
Text_Box.grid(row = 1, column = 1, padx = 20, pady = 10)

submitButton = Button(win, text = 'Submit', font = myFont, command = MorseCode, bg = 'white')
submitButton.grid(row = 3, column = 1)

Exit_Button = Button(win, text = 'Exit', font = myFont, command = close, height = 1, width = 6)
Exit_Button.grid(row = 4, column = 1)

win.mainloop()