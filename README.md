# Simple_Stopwatch_python_tkinter_GUI
Here is a simple creation of a python based GUI stopwatch using tkinter module and some other modules.

code is done in python so pyhton is must.



import tkinter 
import time
import sys
must import this modules in the software you are using.

Also the iconbitmap lined code needs the location of the .ico formatted image for the title in the window 
please remove mine link and provide your own for the code to work or just remove the iconbitmap function from the code
or, use this instead

   def __init__(self):
        self.root=Tk()
        self.root.title("Stop Watch")
        self.root.geometry("550x200")
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t,font=("algerian 40 bold"),bg="light blue")
        self.buttont1 = Button(self.root,text="Start",command=self.start,font=("Times 12 bold"),bg=("Purple"))
        self.buttont2 = Button(self.root,text="Pause",command=self.stop,font=("Times 12 bold"),bg=("red"))
        self.buttont3 = Button(self.root,text="Reset",command=self.reset,font=("Times 12 bold"),bg=("orange"))
        self.buttont4 = Button(self.root, text="Exit", command=self.close,font=("Times 12 bold"),bg=("yellow"))
        self.lb.place(x=160,y=10)
        self.buttont1.place(x=120,y=100)
        self.buttont2.place(x=220,y=100)
        self.buttont3.place(x=320,y=100)
        self.buttont4.place(x=420,y=100)
        self.label = Label(self.root,text="",font=("Times 40 bold"))
        self.root.configure(bg='black')
        self.root.mainloop()



further process can be done according to or copying the main.py from the repositry to the software you are using.
Have fun.

please provide suggestions which can be done in the code

