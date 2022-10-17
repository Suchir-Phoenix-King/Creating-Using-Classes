# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:12:16 2022

@author: PC_RC
"""

from tkinter import *

root = Tk()
root.title("Creating using Classes")
root.geometry("900x600")
root.configure(background="lightblue")


class CreateElements:
    
    def __init__(self):
        print("This is CreateElements class")
        
    def createNewElements(self):
        label = Label(root, text = "YOU HAVE CREATED A LABEL & BUTTON USING THIS HOLY BUTTON", fg = "gold", bg = "lightblue")
        label.pack()
        btn = Button(root, text = " Creation of the HOLY BUTTON ", command = self.message, bg = "gold")
        btn.pack(padx = 20, pady = 10)
        
        
    def message(self):
        print("YOU HAVE CREATED ME, A BUTTON USING THE HOLY BUTTON")


obj_of_CreateElements = CreateElements()

btn = Button(root, text = "I AM THE HOLY BUTTON. CLICK ME", command = obj_of_CreateElements.createNewElements)
btn.pack(padx = "10", pady = "20")

root.mainloop()
