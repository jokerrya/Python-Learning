# import tkinter
from tkinter.simpledialog import askinteger, askfloat, askstring
from tkinter import * 
import tkinter as tk

win = Tk()
menubar =tk.Menu(win)
class WindowsDesc:
    def __init__(self):
        # add title
        win.title("Count Restauant People V1.0") 
        # setting windows size
        win.geometry("600x400") 
        # create menu       
        win.config(menu=menubar)
        # add filemenu
        menu1=tk.Menu(menubar,tearoff=False)
        # add New option
        for item in ["New","Update","Exit"]:
            if item=="Exit":
                menu1.add_separator()#添加一个分割线
                menu1.add_command(label=item,command=lambda :win.quit())#lambda:win.quit==win.quit
            else:
                menu1.add_command(label=item,command=new_action)
        # add help helpmenu
        menubar.add_cascade(label="Open",menu=menu1)
        b = tk.Button(text=var_string)
        b.pack()
        win.mainloop()
var_string ="a"      
def new_action():
    var_string = askstring("Restauant Name",
                           prompt = "Please Input：")


WindowsDesc()
print(new_action())