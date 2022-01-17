# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:57:44 2020

@author: jeffa
"""

import tkinter as tk
import random
from pygame import mixer
import threading
from datetime import datetime
import time 

duration = 45*60
timerRunning = True

def countdown(count):    
    # Exit fuction if the top button is pressed, otherwise continue with countdown
    if timerRunning:
         lbl_timer['text'] = "Time Remaining: " + str(count) + " s"         
         end_time = datetime.fromtimestamp(time.time()+count).strftime("%H:%M:%S")
         clk_time['text'] = end_time
    else:        
        enterButton.config(state=tk.NORMAL)
        return
    
    if count > 0:
        root.after(1000, countdown, count-1)
    elif(count == 0):        
        
        # Quotes for display
        q1 = "\"The World Belongs to Those Who Hustle\""
        
        q2 = "\"I Do My Duty: Other Things Trouble Me Not.\"  \n --Marcus Aurelius"
        
        q3 = "\"I’m a greater believer in luck, and I find the harder I work the more I have of it.\"  \n --Thomas Jefferson"
                
        q4 = "\"Things may come to those who wait, but only the things left by those who hustle.\" \n --Abraham Lincoln"
        
        q5 = "\"Determine never to be idle. No person will have occasion to complain of the want of time who never loses any. It is wonderful how much may be done if we are always doing.\"  \n --Thomas Jefferson"
        
        q6 = "\"Those who love their arts exhaust themselves in working at them...And such men, when they have an emotional attachement to a thing choose neither to eat or sleep rather than to perfect the things for which they care.\"  \n --Marcus Aurelius"
                
        q7 = "\"...remember that what does the work of a fig-tree is a fig-tree, and that what does the work of a dog is a dog, and that what does the work of a bee is a bee, and that what does the work of a man is a man.\" \n --Marcus Aurelius"                            
        
        q8 = " \"Our...aim will be to avoid working either for pointless ends or pointlessly, that is, to avoid desiring what we cannot acheive, or what, once attained, will make us realize too late and after much sweat the emptiness of our desires.\" \n --Seneca"
                     
        q9= "\"Work is the sustenance of noble minds.\"  \n --Seneca"
        
        q10= "\"Do you wish to be useful, or to be praised?\" \n --Epictetus"
        
        q11 = "\"Use the present thoughtfully and justly, for life is short.\"  \n --Marcus Aurelius"

        quotes = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]     
        
        # Play alert and display random quote when timer ends
        mixer.init()
        mixer.music.load("voy_redalert.mp3")
        mixer.music.play()
        lbl_quote['text'] = random.choice(quotes)  
        # Enable enter button when timer ends
        enterButton.config(state=tk.NORMAL)
 
def SetDuration():
    '''Set the timer duration'''
    
    global duration
    # Get duration from input box and convert to int
    strDuration = inputTime.get(1.0, "end-1c")
    duration = int(strDuration)    
    # Set timer label to duration entered
    lbl_timer.config(text="Timer Duration: " + str(duration) + "s")
    # Make sure the start button is enabled
    startButton.config(state=tk.NORMAL) 
        
def StartCountdown():
    global timerRunning
    timerRunning = True
    # Distable start, enter buttons and enable the stop button while the timer is running
    startButton.config(state=tk.DISABLED) 
    enterButton.config(state=tk.DISABLED)    
    stopButton.config(state=tk.NORMAL)
    # Call the timer countdown function
    #countdown(duration)    
    # Create and launch a thread 
    t = threading.Thread (target = countdown(duration))
    t.start()
 
def stopCountdown():
    global timerRunning
    # Set timer running flag to false upon stop button press
    timerRunning = False    
    # enable start and disable stop buttons
    startButton.config(state=tk.NORMAL)
    stopButton.config(state=tk.DISABLED)
    # Reset timer duration to currently stored value
    lbl_timer.config(text="Timer Duration: " + str(duration) + "s")
    lbl_quote['text']=''
    clk_time['text'] = ''

root = tk.Tk()
root.title("Simple Timer with Quotes")

# Configure main window size and position in middle of the screen
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#=======================================FRAMES====================================================
Top = tk.Frame(root, width=500, bd=1, relief=tk.SOLID)
Top.pack(side=tk.TOP)
TextField = tk.Frame(root)
TextField.pack(side=tk.TOP)
BtnGroup = tk.Frame(root, width=500)
BtnGroup.pack(side=tk.BOTTOM)
 
#=======================================LABEL WIDGETS=============================================
 
lbl_title = tk.Label(Top, width=500, text="Quotable Timer", font=('times new roman', 16), fg='green')
lbl_title.pack(fill=tk.X)
lbl_timer = tk.Label(TextField, text="Timer Duration: " + str(duration) + " s", font=('arial', 16))
lbl_timer.pack()
clk_time = tk.Label(TextField, text="", font=('arial', 13), fg='red')
clk_time.pack()  
lbl_quote = tk.Label(root, text="", font=('arial', 16), wraplength=300)
lbl_quote.pack()

#=======================================Button WIDGETS=============================================
inputTime = tk.Text(BtnGroup, height = 1, width = 5)    # Input TextBox 
enterButton = tk.Button(BtnGroup, text = "Enter", command = SetDuration) # Input Button 
inputLabel = tk.Label(BtnGroup, text="Input Timer Duration (s):") # Input Label
startButton = tk.Button(BtnGroup, text="Start Timer", command=StartCountdown)
stopButton = tk.Button(BtnGroup, text="Stop/Reset", command=stopCountdown, fg='red')
stopButton.config(state=tk.DISABLED) # initially disable stop

# set layout of buttons in button frame
inputLabel.grid(row=0, column=1, sticky="ew")
inputTime.grid(row=0, column=2, sticky="ew")
enterButton.grid(row=0, column=3, sticky="ew")
startButton.grid(row=1, column=2, sticky="ew")
stopButton.grid(row=1, column=3, sticky="ew")


#=======================================INITIALIZATION=============================================
if __name__ == '__main__':
    root.mainloop()