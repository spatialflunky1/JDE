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

root = Tk()
scrollbar = Scrollbar(root)
side_scrollbar = Scrollbar(root, orient="horizontal")
textbox = Text(root)
scrollbar.pack(side=RIGHT, fill=Y)
side_scrollbar.pack(side=BOTTOM, fill=X)
textbox.pack(side=BOTTOM, fill=BOTH, expand=1)
scrollbar.config(command=textbox.yview)
side_scrollbar.config(command=textbox.xview)
textbox.config(yscrollcommand=scrollbar.set)
textbox.config(xscrollcommand=side_scrollbar.set)
textbox.insert(END, "Click here to type\n")
root.geometry("800x600")
app = Window(root)
app.draw()
root.mainloop()
