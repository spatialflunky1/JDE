from tkinter import *
import time
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.default_speed = 10
        self.draw()
    def close_window(self):
        self.master.destroy()
    def draw(self):
        self.master.title("JDE")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Exit", command = self.close_window)
        quitButton.place(x=0, y=0)
    def resize_to(self, target_resolution):
      tar_x, tar_y = target_resolution
      target_resolution_string = str(tar_x) + 'x' + str(tar_y)
      self.master.geometry(target_resolution_string)