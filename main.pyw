from tkinter import *
from PIL import ImageTk, Image
import tkinter.filedialog as tkf
import tkinter.messagebox as msgbox
import time
import tkinter.ttk as ttk
from options import *
import os
from pytext import pythings

interpreter = ''
def settitle(title):
    root.title("JDE" + ": " + title)
def popup(event):
    rightclickmenu.tk_popup(event.x_root, event.y_root)
def retrieve():
    input = textbox.get("1.0",END)
    return input
def save(event):
    global filepath
    if filepath == "":
        saveas()
    else:
        with open(filepath,'w') as newfile:
            newfile.write(retrieve())
            parselist = str(filepath).split("/")
            settitle(parselist[-1])
            print(filepath)
def saveas():
    global filepath
    files = [('Python Files', '*.py *.pyw'), ('Text File', '*.txt'), ('All Files', '*.*')]
    file = tkf.asksaveasfile(filetypes = files, defaultextension = files)
    parselist = str(file).split('\'')
    with open(parselist[1],'w') as newfile:
        newfile.write(retrieve())
    filepath = newfile.name
    parseplist = str(filepath).split('/')
    settitle(parseplist[-1])
def openfile():
    global filepath
    try:
        files = [('Python Files', '*.py *.pyw'), ('Text File', '*.txt'), ('All Files', '*.*')]
        file = tkf.askopenfile(filetypes = files, defaultextension = files)
        parselist = str(file).split('\'')
        with open(parselist[1],'r') as thefilename:
            filepath = thefilename.name
            x = thefilename.read()
            parseplist = str(filepath).split('/')
            settitle(parseplist[-1])
            textbox.delete(1.0, END)
            textbox.insert(INSERT, x)
            color(True)
    except:
        print("No file selected")
def new():
    global filepath
    filepath = ""
    settitle("NewFile")
    textbox.delete(1.0, END)
def copy(event=None):
    root.clipboard_clear()
    text = root.selection_get()
    root.clipboard_append(text)
def paste(event=None):
    text = root.selection_get(selection='CLIPBOARD')
    textbox.insert('insert', text)
    textbox.delete("sel.first", "sel.last")
def cut(event=None):
    copy()
    textbox.delete("sel.first", "sel.last")
def select_all(event=None):
    textbox.tag_add('sel', '1.0', 'end')
def undoo(event=None):
    textbox.edit_undo()
#    textbox.edit_separator()
def redoo(event=None):
    textbox.edit_redo()
def find():
    global searchbox
    textbox.tag_remove('found', '1.0', END)
    s = searchbox.get()
    if s:
        idx = '1.0'
        while 1:
            idx = textbox.search(s, idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))
            textbox.tag_add('found', idx, lastidx)
            idx = lastidx
        textbox.tag_config('found', foreground = 'red')
def findreplace():
        global searchrbox
        global replacebox
        textbox.tag_remove('found', '1.0', END)
        s = searchrbox.get()
        f = replacebox.get()
        if s:
            idx = '1.0'
            while 1:
                idx = textbox.search(s, idx, nocase=1, stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))
                textbox.tag_add('found', idx, lastidx)
                idx = lastidx
            textbox.replace("found.first", "found.last", f)
def findreplacebox():
    global searchrbox
    global replacebox
    newbox = Toplevel(root)
    newbox.title("Find and Replace")
    newbox.resizable(False, False)
    searchrbox = Entry(newbox)
    searchrbox.pack(side=LEFT, fill=BOTH, expand=1)
    searchrbox.insert(END, "Find")
    replacebox = Entry(newbox)
    replacebox.pack(side=LEFT, fill=BOTH, expand=1)
    replacebox.insert(END, "Replace")
    okbutton = Button(newbox, text = "Ok",  command = newbox.destroy)
    okbutton.pack(side=RIGHT)
    findreplacebutton = Button(newbox, text = "Replace",  command =lambda : findreplace())
    findreplacebutton.pack(side=RIGHT)
def findbox():
    global searchbox
    newbox = Toplevel(root)
    newbox.title("")
    newbox.resizable(False, False)
    searchbox = Entry(newbox)
    searchbox.pack(side=LEFT, fill=BOTH, expand=1)
    okbutton = Button(newbox, text = "Ok",  command = newbox.destroy)
    okbutton.pack(side=RIGHT)
    findbutton = Button(newbox, text = "Find",  command =lambda : find())
    findbutton.pack(side=RIGHT)
def aboutbox():
    global aboutwin
    try:
        if aboutwin.state() == "normal":
            aboutwin.focus()
    except:
        aboutwin = Toplevel(root)
        aboutwin.title("About")
        aboutwin.resizable(False, False)
        aboutwin.geometry("465x350")
        nm = Label(aboutwin, text="JDE", fg='deep sky blue')
        nm.configure(font=("Segoe UI", 16, "bold"))
        nm.pack()
        nm.place(rely=1, relx=1, x=-245, y=-160, anchor=S)

        nms = Label(aboutwin, text="Jakes Development Environment")
        nms.configure(font=("Segoe UI", 14))
        nms.pack()
        nms.place(rely=1, relx=1, x=-245, y=-130, anchor=S)

        ds = Label(aboutwin, text="An Integrated Development \nEnvironment to code Python and others in the future.")
        ds.configure(font=("Segoe UI", 12))
        ds.pack()
        ds.place(rely=1, relx=1, x=-245, y=-75, anchor=S)

        wb = Label(aboutwin, text="Developed by:")
        wb.configure(font=("Segoe UI", 12))
        wb.pack()
        wb.place(rely=1, relx=1, x=-280, y=-35, anchor=S)

        db = Label(aboutwin, text="Spatialflunky1", fg="dodger blue")
        db.configure(font=("Segoe UI", 12))
        db.pack()
        db.place(rely=1, relx=1, x=-175, y=-35, anchor=S)

        vs = Label(aboutwin, text=version)
        vs.configure(font=("Segoe UI", 10))
        vs.pack()
        vs.place(rely=1, relx=1, x=-245, y=-5, anchor=S)

        okbutton = ttk.Button(aboutwin, text = "OK",  command = aboutwin.destroy)
        okbutton.pack()
        okbutton.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

        load = Image.open(aboutbanner)
        render = ImageTk.PhotoImage(load)
        img = Label(aboutwin, image=render)
        img.image = render
        img.place(x=0, y=0)
def fontsizeset():
    global sizebox
    global defaultfont
    global fontsize
    fontsize = sizebox.get()
    textbox.configure(font=(defaultfont, fontsize))
def fontsizebox():
    global fontsizewin
    global sizebox
    try:
        if fontsizewin.state() == "normal":
            fontsizewin.focus()
    except:
        newbox = Toplevel(root)
        newbox.title("Size")
        newbox.resizable(False, False)
        sizebox = Entry(newbox)
        sizebox.pack(side=LEFT, fill=BOTH, expand=1)
        okbutton = Button(newbox, text = "OK",  command = newbox.destroy)
        okbutton.pack(side=RIGHT)
        sizebutton = Button(newbox, text = "Set Size",  command =lambda : fontsizeset())
        sizebutton.pack(side=RIGHT)
def fontchange(font):
    global defaultfont
    global fontsize
    textbox.configure(font=(font, fontsize))
    defaultfont = font
def tab(arg):
    textbox.insert(INSERT, "    ")
    return 'break'
def run():
    parselist = str(filepath).split('/')
    parseplist = parselist[-1].split('.')
    if(filepath == ''):
        msgbox.showerror('Error!', 'No File Selected')
    elif(parseplist[-1] != "py" and parseplist[-1] != "pyw"):
        msgbox.showerror('Error!', 'File is not a python file')
    else:
        path = '"' + filepath + '"'
        os.system("start python " + path)
        print(path)
def typed(event):
    parselist = root.title()[-1]
    if(parselist == "*"):
        return 
    else:
        root.title(root.title() + "*")
def on_closing():
    if(root.title()[-1] == "*"):
        if msgbox.askquestion("File Not Saved", "Do you still want to quit?") == "yes":
            root.destroy()
        else:
            return
    else:
        root.destroy()
def color(event):
    if "if ":
        idx = '1.0'
        while 1:
            idx = textbox.search("if ", idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len("if "))
            textbox.tag_add('xif', idx, lastidx)
            idx = lastidx
            textbox.tag_config('xif', foreground = 'yellow')
    if "elif ":
        idx = '1.0'
        while 1:
            idx = textbox.search("elif ", idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len("elif "))
            textbox.tag_add('xelif', idx, lastidx)
            idx = lastidx
            textbox.tag_config('xelif', foreground = 'yellow')
    if "else ":
        idx = '1.0'
        while 1:
            idx = textbox.search("else ", idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len("else "))
            textbox.tag_add('xelse', idx, lastidx)
            idx = lastidx
            textbox.tag_config('xelse', foreground = 'yellow')
    if "def ":
        idx = '1.0'
        while 1:
            idx = textbox.search("def ", idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len("def "))
            textbox.tag_add('xdef', idx, lastidx)
            idx = lastidx
            textbox.tag_config('xdef', foreground = 'cyan')
    if "import ":
        idx = '1.0'
        while 1:
            idx = textbox.search("import ", idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len("import "))
            textbox.tag_add('xim', idx, lastidx)
            idx = lastidx
            textbox.tag_config('xim', foreground = 'magenta')
    if "from ":
        idx = '1.0'
        while 1:
            idx = textbox.search("from ", idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len("from "))
            textbox.tag_add('xfr', idx, lastidx)
            idx = lastidx
            textbox.tag_config('xfr', foreground = 'magenta')
    if "in ":
        idx = '1.0'
        while 1:
            idx = textbox.search("in ", idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len("in "))
            textbox.tag_add('xin', idx, lastidx)
            idx = lastidx
            textbox.tag_config('xin', foreground = 'magenta')
    if "class ":
        idx = '1.0'
        while 1:
            idx = textbox.search("class ", idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len("class "))
            textbox.tag_add('xclass', idx, lastidx)
            idx = lastidx
            textbox.tag_config('xclass', foreground = 'cyan')


filepath = ""
root = Tk()
root.title("JDE: NewFile")
root.configure(bg = 'gray25')
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command =lambda : new())
filemenu.add_command(label="Open", command =lambda : openfile())
filemenu.add_command(label="Save", command =lambda : save())
filemenu.add_command(label="Save As...", command=lambda : saveas())
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Copy                     Ctrl + C", command =lambda : copy())
editmenu.add_command(label="Cut                        Ctrl + Z", command =lambda :cut())
editmenu.add_command(label="Paste                     Ctrl + V", command =lambda : paste())
editmenu.add_command(label="Select All               Ctrl + A", command =lambda : select_all())
editmenu.add_command(label="Undo                     Ctrl + Z", command =lambda : undoo())
editmenu.add_command(label="Redo                      Ctrl + Y", command =lambda : redoo())
editmenu.add_command(label="Find", command =lambda : findbox())
editmenu.add_command(label="Find & Replace", command =lambda : findreplacebox())
menubar.add_cascade(label="Edit", menu=editmenu)

formatmenu = Menu(menubar, tearoff=0)
fontmenu = Menu(formatmenu, tearoff=0)
fontmenu.add_command(label="Arial", command =lambda : fontchange("Arial"))
fontmenu.add_command(label="Times New Roman", command =lambda : fontchange("Times"))
fontmenu.add_command(label="Consolas", command =lambda : fontchange("Consolas"))
fontmenu.add_command(label="Courier New", command =lambda : fontchange("Courier"))
fontmenu.add_command(label="Fixedsys", command =lambda : fontchange("Fixedsys"))
fontmenu.add_command(label="Comic Sans MS", command =lambda : fontchange("Comic Sans MS"))
fontmenu.add_command(label="MS Sans Serif", command =lambda : fontchange("MS Sans Serif"))
fontmenu.add_command(label="MS Serif", command =lambda : fontchange("MS Serif"))
fontmenu.add_command(label="Monaco", command =lambda : fontchange("Monaco"))
fontmenu.add_command(label="Symbol", command =lambda : fontchange("Symbol"))
fontmenu.add_command(label="System", command =lambda : fontchange("System"))
fontmenu.add_command(label="Verdana", command =lambda : fontchange("Verdana"))
formatmenu.add_command(label="Size", command =lambda : fontsizebox())
formatmenu.add_cascade(label="Font", menu=fontmenu)
menubar.add_cascade(label="Format", menu=formatmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command =lambda : aboutbox())
menubar.add_cascade(label="Help", menu=helpmenu)

rightclickmenu = Menu(menubar, tearoff=0)
rightclickmenu.add_command(label="Copy", command =lambda : copy())
rightclickmenu.add_command(label="Cut", command =lambda : cut())
rightclickmenu.add_command(label="Paste", command =lambda: paste())
rightclickmenu.add_command(label="Select All", command =lambda : select_all())
rightclickmenu.add_command(label="Undo", command =lambda : undoo())
rightclickmenu.add_command(label="Redo", command =lambda : redoo())
root.bind("<Button-3>", popup)
root.bind("<Control-z>", undoo)
root.bind("<Control-y>", redoo)
root.bind("<Control-s>", save)
#root.bind("<Control-y>", lambda : fontsizeinc())
root.config(menu=menubar)
root.protocol("WM_DELETE_WINDOW", on_closing)
runimage = PhotoImage(file = r"run.png")
runbutton = Button(root, image = runimage, command = lambda : run())
runbutton.pack()
scrollbar = Scrollbar(root)
side_scrollbar = Scrollbar(root, orient="horizontal")
textbox = Text(root, undo=True)
textbox.bind("<Tab>", tab)
textbox.configure(bg = 'gray19', fg = 'white')
textbox.configure(insertbackground='white')
textbox.bind("<Key>", typed)
textbox.bind("<Key>", color)
scrollbar.pack(side=RIGHT, fill=Y)
side_scrollbar.pack(side=BOTTOM, fill=X)
textbox.pack(side=BOTTOM, fill=BOTH, expand=1)
scrollbar.config(command=textbox.yview)
side_scrollbar.config(command=textbox.xview)
textbox.config(yscrollcommand=scrollbar.set)
textbox.config(xscrollcommand=side_scrollbar.set)
textbox.configure(font=(defaultfont, fontsize))
textbox.insert(END, "Click here to type\n")
root.iconbitmap(default=icon)
root.geometry(windowsize)
root.mainloop()
