#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:12:58 2021

@author: sage
"""
import os  
from PIL import Image, ImageTk  
import tkinter as tk
from hw_1 import Process

#resizing the initial pic
def resize(pil_image, w_box, h_box): 
    w, h = pil_image.size  
    f1 = 1.0*w_box/w
    f2 = 1.0*h_box/h  
    factor = min(f1, f2)  
    width = int(w*factor)  
    height = int(h*factor)  
    return pil_image.resize((width, height), Image.ANTIALIAS)  

#define button to show result
def hit_me():
    global w_box
    global h_box
    global label2
    global transfered_image
    progress = Process('Adele.jpg')
    progress.respon()
    progress.decode()
    pil_image = Image.open('1.jpg')   
    pil_image_resized = resize(pil_image, w_box/2, h_box) 
    transfered_image = ImageTk.PhotoImage(pil_image_resized)
    label2=tk.Label(root, image=transfered_image, width=w_box/2, height=h_box)
    label2.pack(side = tk.RIGHT)
    
#creat a window with a button
root = tk.Tk() 
root.title('Transfer')
w_box = 600  
h_box = 500 
root.geometry(str(w_box)+'x'+str(h_box))
b = tk.Button(root, text='transfer', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()

#put pics into the window
pil_image = Image.open('Adele.jpg')
pil_image_resized = resize(pil_image, w_box/2, h_box)  
image = ImageTk.PhotoImage(pil_image_resized)  
label1=tk.Label(root, image=image, width=w_box/2, height=h_box)
label1.pack(side = tk.LEFT)
root.mainloop()