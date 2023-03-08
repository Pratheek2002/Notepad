# Note pad using tkinter

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os


def change_cursor(event):
    event.widget.configure(cursor="hand2")



def newfile():
    global file
    root.title("Untitled--Notepad")
    file=None
    textarea.delete(1.0 , END) #1.0 means 1st line 0th charcacter to end character


def openfile():
    global file
    file=askopenfilename(defaultextension=".txt" , filetypes=[("Allfiles","*.*"),("Textdocuments" , "*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + "-- Notepad")
        textarea.delete(1.0, END)
        f=open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt" , filetypes=[("Allfiles","*.*"),("Textdocuments" , "*.txt")])
        if file=="":
            file=None
        else: #save as a new file
            f=open(file,"w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-- Notepad")
            print("FIle saved")
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    showinfo("About Notepad","Notepad is created by Pratheek")


if __name__ == '__main__':
    # tkintet setup
    root = Tk()
    root.title("Untitled -- Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("800x600")

    # text area

    textarea = Text(root, font="lucida 13")
    file=None
    textarea.pack(fill=BOTH ,expand=True)  #expand works as a when it expands text area also increases with it

    #menu bar
    menubar=Menu(root)

    # File menu

    Filemenu=Menu(menubar,tearoff=0)
    Filemenu.add_command(label="New" ,command=newfile)     #new
    Filemenu.add_command(label="Open", command=openfile)   #existing file
    Filemenu.add_command(label="Save" , command=savefile)  #save file
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit", command=quitapp)

    menubar.add_cascade(label="File", menu=Filemenu)
    root.config(menu=menubar)

    #edit menu

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=cut)          # cut
    editmenu .add_command(label="Copy", command=copy)       #copy
    editmenu.add_command(label="Paste", command=paste)     # paste

    menubar.add_cascade(label="Edit", menu=editmenu)
    root.config(menu=menubar)

    #help

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About Notepad", command=about)  # About notepad

    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)

    #Adding scroll bar
    scrollbar=Scrollbar(textarea)
    scrollbar.pack(side=RIGHT , fill=Y)
    scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)
    scrollbar.bind("<Enter>", change_cursor)


    root.mainloop()
