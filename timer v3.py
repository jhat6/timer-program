# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:57:44 2020

@author: jeffa
"""

import tkinter as tk
import random


DURATION = 2

def countdown(count):    
    lbl_text['text'] = "Time Remaining: " + str(count) + " s"
    if count > 0:
        root.after(1000, countdown, count-1)
    elif(count == 0):        
        
        q1 = "\"The World Belongs to Those Who Hustle\""
        
        q2 = "\"I Do My Duty: Other Things Trouble Me Not.\"  \n --Marcus Aurelius"
        
        q3 = "\"I’m a greater believer in luck, and I find the harder I work \
            the more I have of it.\"  \n --Thomas Jefferson"
                
        q4 = "\"Things may come to those who wait, but only the things left by \
            those who hustle.\" \n --Abraham Lincoln"
        
        q5 = "\"Determine never to be idle. No person will have occasion to \
            complain of the want of time who never loses any. It is wonderful \
                how much may be done if we are always doing.\"  \n --Thomas Jefferson"
        
        q6 = "\"Those who love their arts exhaust themselves in working at \
            them...And such men, when they have an emotional attachement to a \
                thing choose neither to eat or sleep rather than to perfect \
                    the things for which they care.\"  \n --Marcus Aurelius"
                
        q7 = "\"...remember that what does the work of a fig-tree is a \
            fig-tree, and that what does the work of a dog is a dog, and that \
                what does the work of a bee is a bee, and that what does the \
                    work of a man is a man.\" \n --Marcus Aurelius"                            
        
        q8 = " \"Our...aim will be to avoid working either for pointless ends \
            or pointlessly, that is, to avoid desiring what we cannot acheive, \
                or what, once attained, will make us realize too late and \
                    after much sweat the emptiness of our desires.\" \n --Seneca"
                     
        q9= "\"Work is the sustenance of noble minds.\"  \n --Seneca"
        
        q10= "\"Do you wish to be useful, or to be praised?\" \n --Epictetus"
        
        q11 = "\"Use the present thoughtfully and justly, for life is short.\"  \n --Marcus Aurelius"

        quotes = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]       
        lbl_quote['text'] = random.choice(quotes)  
 
def StartCountdown():
    countdown(DURATION)
    btn_toggle.config(state=tk.DISABLED) 
 
def BackBtn():
    #NewForm.destroy()
    btn_toggle.config(state=tk.NORMAL)
    lbl_text.config(text=str(DURATION))
    lbl_quote['text']=''

root = tk.Tk()
root.title("50 Minute Work Timer")
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
 
lbl_title = tk.Label(Top, width=500, text="Productivity Timer", font=('times new roman', 16))
lbl_title.pack(fill=tk.X)
lbl_text = tk.Label(TextField, text="Timer Duration: " + str(DURATION) + " s", font=('arial', 16))
#lbl_text.pack(fill=tk.BOTH) 
lbl_text.pack() 
 
lbl_quote = tk.Label(root, text="", font=('arial', 16), wraplength=300)
lbl_quote.pack()

#=======================================Button WIDGETS=============================================

#entry1 = tk.Entry(BtnGroup)
#entry1.pack(side = tk.TOP)
btn_toggle = tk.Button(BtnGroup, text="Start Timer", command=StartCountdown)
btn_toggle.pack(side = tk.LEFT )
btn_back = tk.Button(BtnGroup, text="Reset Timer", command=BackBtn)
btn_back.pack(side=tk.LEFT)


#=======================================INITIALIZATION=============================================
if __name__ == '__main__':
    root.mainloop()