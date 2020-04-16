from tkinter import *
import time
<<<<<<< HEAD
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.default_speed = 10
        self.draw()
    def close_window(self):
        self.master.destroy()
    def draw(self):
        self.master.title("IDE Withought a Name")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Exit", command = self.close_window)
        quitButton.place(x=0, y=0)

root = Tk()
scrollbar = Scrollbar(root)
side_scrollbar = Scrollbar(root, orient="horizontal")
textbox = Text(root, height=73, width=70)
=======
import window
import uimanager
ui_manager = uimanager.UIManager(frame = [800,600])
print(ui_manager.is_fullscreen)
root = Tk()
scrollbar = Scrollbar(root)
side_scrollbar = Scrollbar(root, orient="horizontal")
textbox = Text(root)
>>>>>>> origin/dev
scrollbar.pack(side=RIGHT, fill=Y)
side_scrollbar.pack(side=BOTTOM, fill=X)
textbox.pack(side=BOTTOM, fill=BOTH, expand=1)
scrollbar.config(command=textbox.yview)
side_scrollbar.config(command=textbox.xview)
textbox.config(yscrollcommand=scrollbar.set)
textbox.config(xscrollcommand=side_scrollbar.set)
textbox.insert(END, "Click here to type\n")
<<<<<<< HEAD
root.geometry("1920x1080")
app = Window(root)
=======
root.geometry("800x600")
app = window.Window(root)
>>>>>>> origin/dev
app.draw()
root.mainloop()
