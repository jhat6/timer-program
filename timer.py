# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:01:18 2020

@author: jeffa
"""

import time
import tkinter as tk

window = tk.Tk()

print("Input Count Down Time in Seconds: ")
read_time = input()

time_seconds = int(read_time)
print("\n")
for i in range(time_seconds, 0, -1):
    print(i)
    time.sleep(1)


q1 = "The World Belongs to Those Who Hustle"
q2 = "I Do My Duty: Other Things Trouble Me Not.  Marcus Aurelius"
q3 = "I’m a greater believer in luck, and I find the harder I work the more \
        I have of it.  Thomas Jefferson"
q4 = "Things may come to those who wait, but only the things left by those who \
        hustle. Abraham Lincoln"

q5 = "Determine never to be idle. No person will have occasion to complain of \
        the want of time who never loses any. It is wonderful how much may be \
            done if we are always doing.  Thomas Jefferson"

q6 = "Those who love their arts exhaust themselves in working at them...And such men, \
        when they have an emotional attachement to a thing choose neither to eat or sleep rather \
            than to perfect the things for which they care.  Marcus Aurelius"
        
q7 = "...remember that what does the work of a fig-tree is a fig-tree, and that \
         what does the work of a dog is a dog, and that what does the work of a bee is a bee, and \
             that what does the work of a man is a man. Marcus Aurelius"
            
q8 = "Our...aim will be to avoid working either for pointless ends or pointlessly, that is, to avoid \
        desiring what we cannot acheive, or what, once attained, will make us realize too late and after \
            much sweat the emptiness of our desires.  Seneca"

q9= "Work is the sustenance of noble minds.  Seneca"

q10= " Do you wish to be useful, or to be praised? Epictetus"

q11 = "Use the present thoughtfully and justly, for life is short.  Marcus Aurelius"

quotes = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]


text = tk.Label(text=q11)
text.pack()


window.title('My Window')
window.geometry('500x300') 
 
e1 = tk.Entry(window, show=None, font=('Arial', 14))  
e1.pack()
print(e1)
window.mainloop()

