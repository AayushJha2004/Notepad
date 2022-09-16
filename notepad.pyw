from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def new_file():
    global file
    notepad.title("Untitled Notepad")
    file = None
    text.delete(1.0, END)


def open_file():
    global file
    file = askopenfilename(defaultextension=".txt"
                           , filetypes=[("All Files", "*.*"),
                                        ("Text Documents", "*.txt")])
    if file == "None":
        file = None
    else:
        notepad.title(os.path.basename(file) + " - notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()


def save_file():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",
                                 defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                     ("Text Documents", "*.txt")])
        if file == "":
            file == None
        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()
            notepad.title(os.path.basename(file) + " - notepad")
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()


def exit_file():
    notepad.destroy()


def cut_():
    text.event_generate("<<Cut>>")


def copy_():
    text.event_generate("<<Copy>>")


def paste_():
    text.event_generate("<<Paste>>")


def about_():
    showinfo("Notepad", "Your handy Notepad made by Aayush Jha")


if __name__ == '__main__':
    notepad = Tk()
    notepad.geometry("854x480")
    notepad.title("Untitled Notepad")
    notepad.wm_iconbitmap("Icon.ico")
    text = Text(notepad, font="Calibri 12")
    text.pack(expand=True, fill=BOTH)
    file = None

    menu_ = Menu(notepad)

    file_menu = Menu(menu_, tearoff=0)

    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Exit", command=exit_file)
    menu_.add_cascade(label="File", menu=file_menu)

    edit_menu = Menu(menu_, tearoff=0)
    edit_menu.add_command(label="Cut", command=cut_)
    edit_menu.add_command(label="Copy", command=copy_)
    edit_menu.add_command(label="Paste", command=paste_)
    menu_.add_cascade(label="Edit", menu=edit_menu)

    help_menu = Menu(menu_, tearoff=0)
    help_menu.add_command(label="About", command=about_)
    menu_.add_cascade(label="Help", menu=help_menu)

    notepad.config(menu=menu_)

    scroll_bar = Scrollbar(text)
    scroll_bar.pack(side=RIGHT, fill=Y)
    scroll_bar.config(command=text.yview)
    text.config(yscrollcommand=scroll_bar.set)

    notepad.mainloop()
