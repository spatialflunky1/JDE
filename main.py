from tkinter import *
import tkinter.filedialog
import time
import window
import uimanager
def retrieve():
    input = textbox.get("1.0",END)
    return input
def save():
    global filepath
    if filepath == "":
        saveas()
    else:
        with open(filepath,'w') as newfile:
            newfile.write(retrieve())
def saveas():
    global filepath
    global app
    files = [('Python Files', '*.py'), ('Text File', '*.txt'), ('All Files', '*.*')]
    file = tkinter.filedialog.asksaveasfile(filetypes = files, defaultextension = files)
    parselist = str(file).split('\'')
    with open(parselist[1],'w') as newfile:
        newfile.write(retrieve())
    filepath = newfile.name
    app.settitle(filepath)
def openfile():
    global app
    files = [('Python Files', '*.py'), ('Text File', '*.txt'), ('All Files', '*.*')]
    file = tkinter.filedialog.askopenfile(filetypes = files, defaultextension = files)
    parselist = str(file).split('\'')
    with open(parselist[1],'r') as thefilename:
        x = thefilename.read()
        app.settitle(parselist[1])
        textbox.delete(1.0, END)
        textbox.insert(INSERT, x)
def new():
    global app
    app.settitle("NewFile")
    textbox.delete(1.0, END)
def popup(event):
    rightclickmenu.tk_popup(event.x_root, event.y_root)
ui_manager = uimanager.UIManager(frame = [800,600])
# print(ui_manager.is_fullscreen)
filepath = ""
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command =lambda : new())
filemenu.add_command(label="Open", command =lambda : openfile())
filemenu.add_command(label="Save", command =lambda : save())
filemenu.add_command(label="Save As...", command=lambda : saveas())
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
editmenu.add_command(label="Find")
editmenu.add_command(label="Find & Replace")
menubar.add_cascade(label="Edit", menu=editmenu)
rightclickmenu = Menu(menubar, tearoff=0)
rightclickmenu.add_command(label="Copy")
rightclickmenu.add_command(label="Paste")
rightclickmenu.add_command(label="Undo")
rightclickmenu.add_command(label="Redo")
root.bind("<Button-3>", popup)
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
root.geometry("950x430")
app = window.Window(root)
app.draw()
root.mainloop()
