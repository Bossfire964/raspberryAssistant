import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time
import threading

currentRunningTitle = "System Booting Up..."



class App(tk.Frame):
    def __init__(self):
        pass
    def callback(self):
        self.root.quit()
    def updateTitle(self, text):
        self.titleLabel.config(text = text)
    def update(self):
        self.main.update()
        app.root.after(100,self.update)
    def run(self, main):
        self.main = main
        self.root = Tk()
        self.root.geometry("1080x10180")
        # Create a photoimage object of the image in the path
        assistantImage = Image.open("MoneyIcon.png")
        assistantImage = ImageTk.PhotoImage(assistantImage)

        label1 = tk.Label(image=assistantImage)
        label1.image = assistantImage

        self.titleLabel = tk.Label(self.root, text="System Booting Up...",font="Arial 50 bold")
        self.titleLabel.place(x=540, y=50,anchor=CENTER)

        # Position image
        label1.place(x=540, y=350, anchor = CENTER)
        self.update()
        self.root.mainloop()



app = App()




