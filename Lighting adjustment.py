from Tkinter import *
import RPi.GPIO as GPIO
GPIO.setwarnings(False)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)

GPIO.setup(35, GPIO.OUT)

GPIO.setup(37, GPIO.OUT)

GPIO.setup(07, GPIO.OUT)

GPIO.setup(11, GPIO.OUT)

GPIO.setup(13, GPIO.OUT)

GPIO.setup(15, GPIO.OUT)

GPIO.setup(29, GPIO.OUT)
GPIO.setwarnings(False)

menu = Menu(root)
root.config(menu=menu)

def high_brightness():
    
    GPIO.output(29,True)
    GPIO.output(15,True)            
    GPIO.output(11,True)
    GPIO.output(13,True)
    GPIO.output(07,True)

def normal_brightness():
    GPIO.output(29,True)
    GPIO.output(15,True)            
    GPIO.output(11,True)
    GPIO.output(13,False)
    GPIO.output(07,False)


def low_brightness():

    GPIO.output(29,True)
    GPIO.output(15,False)            
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(07,False)


def dark():

    GPIO.output(29,False)
    GPIO.output(15,False)            
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(07,False)


def red_color():

    GPIO.output(31,False)
    GPIO.output(35,True)
    GPIO.output(37,False)


def yellow_color():

    GPIO.output(31,True)
    GPIO.output(35,False)
    GPIO.output(37,False)


def green_color():

    GPIO.output(31,False)
    GPIO.output(35,False)
    GPIO.output(37,True)


def no_color():

    GPIO.output(31,False)
    GPIO.output(35,False)
    GPIO.output(37,False)

Brightness = Menu(menu)
menu.add_cascade(label="Adjust white light brightness", menu=Brightness)
Brightness.add_command(label="High Brightness", command=high_brightness)

Brightness.add_separator()

Brightness.add_command(label="Normal Brightness", command=normal_brightness)

Brightness.add_separator()
Brightness.add_command(label="Low Brightness", command=low_brightness)
Brightness.add_command(label="Turn off white light", command=dark)

Color = Menu(menu)

menu.add_cascade(label="Color ights", menu=Color)
Color.add_command(label="Red light", command=red_color)

Color.add_command(label="yellow light", command=yellow_color)


Color.add_command(label="Green light", command=green_color)

Color.add_separator()

Color.add_command(label="No color", command=no_color)
