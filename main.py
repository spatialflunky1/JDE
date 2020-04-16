from tkinter import *
import time
import window
import uimanager
ui_manager = uimanager.UIManager(frame = [800,600])
print(ui_manager.is_fullscreen)
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
app = window.Window(root)
app.draw()
root.mainloop()
