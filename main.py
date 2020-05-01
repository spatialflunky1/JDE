from tkinter import *
from tkinter.filedialog import asksaveasfile
import time
import window
import uimanager
def retrieve():
    input = textbox.get("1.0",END)
    return input
def saveas():
    files = [('Python Files', '*.py'), ('Text File', '*.txt'), ('All Files', '*.*')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
    parselist = str(file).split('\'')
    with open(parselist[1],'w') as newfile:
        newfile.write(retrieve())
#def openfile():
#    return
ui_manager = uimanager.UIManager(frame = [800,600])
# print(ui_manager.is_fullscreen)
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As...", command=lambda : saveas())
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
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

# print(input)
root.geometry("800x600")
app = window.Window(root)
app.draw()
root.mainloop()
