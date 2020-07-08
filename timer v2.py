# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:20:22 2020

@author: jeffa
"""

import tkinter as tk
import time 

timer = tk.Tk()

canvas1 = tk.Canvas(timer, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(timer, text='Productivity Timer')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(timer, text='Enter Time in Seconds:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (timer) 
canvas1.create_window(200, 140, window=entry1)

def count_down_timer ():
    
    print("test")
    
    text1 = "Time Remaining:"
    label3 = tk.Label(timer, text= text1,font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)    
    
    # for time_remaining in range(int(time_seconds), 0, -1):
    #     print(time_remaining)
    #     label4 = tk.Label(timer, text= str(time_remaining),font=('helvetica', 10, 'bold'))
    #     canvas1.create_window(200, 230, window=label4)
    #     time.sleep(1)    

    
button1 = tk.Button(text='Start Timer', command=count_down_timer, bg='brown', \
                    fg='white', font=('helvetica', 9, 'bold'))
time_seconds = entry1.get()
print(time_seconds)
canvas1.create_window(200, 180, window=button1)

timer.mainloop()