#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:48:42 2018

@author: afar
"""

import tkinter

window = tkinter.Tk()

window.title("LocalVoip")

window.geometry("300x300")

#window.iconbitmap("")

lbl =    tkinter.Label(window, text="Label")

lbl.pack()

etr = tkinter.Entry(window)

etr.pack()

btn = tkinter.Button(window, text="Button")

btn.pack()

window.configure(background="#AED84C")

                
window.mainloop()


