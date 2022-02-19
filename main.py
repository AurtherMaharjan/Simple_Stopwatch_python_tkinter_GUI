import tkinter
from tkinter import *
import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb
from PIL import Image, ImageTk


def open_window():
    read = easygui.fileopenbox()
    return read

def open_file():
    string = open_window()
    try:
        os.startfile(string)
        return filedialog.askopenfilename()
    except:
        mb.showinfo('confirmation', "File not found!")



def copy_file():
    try:
        source1=open_window()
        destination1=filedialog.askdirectory()
        shutil.copy2(source1,destination1)
        mb.showinfo("confirmation", "File copied")
    except FileNotFoundError:
        mb.showinfo("confirmation", "File Not Copied")



def delete_file():
    try:
        del_file = open_window()
        os.path.exists(del_file)
        os.remove(del_file)
        mb.showinfo("confirmation", "File Deleted.")
    except:
        mb.showinfo("confirmation", "File do not exist")

def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension=os.path.splitext(chosenFile)[1]
    print("Enter new name for the file")
    newName=input()
    path=os.path.join(path1, newName+extension)
    print(path)
    os.rename(chosenFile,path)
    mb.showinfo("confirmation", "File Renamed Successfully")

def move_file():
    try:
        source=open_window()
        destination=filedialog.askdirectory()
        if(source==destination):
            mb.showinfo("confirmation", "Source And Destination Are Same")
        else:
            shutil.move(source, destination)
            mb.showinfo("confirmation", "File Moved Successfully")
    except FileNotFoundError:
        mb.showinfo("confirmation", "File Not Moved")

def make_folder():
    newFolderPath=filedialog.askdirectory()
    print("Enter the name of the new folder")
    newFolder=input()
    path=os.path.join(newFolderPath, newFolder)
    os.mkdir(path)
    mb.showinfo("confirmation", "New Folder created")

def remove_folder():
    try:
            delFolder=filedialog.askdirectory()
            os.rmdir(delFolder)
            mb.showinfo("confirmation", "Folder deleted Successfully")
    except OSError:
        mb.showinfo("confirmation", "Folder Not Empty")


def list_files():
    try:
        folderList=filedialog.askdirectory()
        sortlist=sorted(os.listdir(folderList))
        i=0
        print("files in ", folderList, "folder are:")
        while(i<len(sortlist)):
            print(sortlist[i]+"\n")
            i+=1
    except FileNotFoundError:
        mb.showinfo("confirmation", "No Files You Looking For!")



root=Tk()

canv=Canvas(root, width=400, height=300, bg="lightblue")
canv.grid(row=0, column=2)

img = ImageTk.PhotoImage(Image.open(r"C:\Users\kenda\PycharmProjects\filemanager\filemanager.ico"))
canv.create_image(180, 150, anchor=tkinter.CENTER, image=img)

root.iconbitmap("C:\\Users\\kenda\\PycharmProjects\\filemanager\\filemanager.ico")
root.title("File Manager")
root.resizable(False, False)

Label(root, text="File Manager" "\n", font=("Times", 16),
fg="blue").grid(row = 5, column = 2,)

Button(root, text="Open a File", bg="lightgreen", command = open_file).grid(row=15, column =2)
Button(root, text = "Copy a File", bg="lightgreen", command = copy_file).grid(row = 25, column = 2)
Button(root, text = "Delete a File", bg="lightgreen", command = delete_file).grid(row = 35, column = 2)
Button(root, text = "Rename a File", bg="lightgreen", command = rename_file).grid(row = 45, column = 2)
Button(root, text = "Move a File", bg="lightgreen", command = move_file).grid(row = 55, column =2)
Button(root, text = "Make a Folder", bg="lightgreen", command = make_folder).grid(row = 75, column = 2)
Button(root, text = "Remove a Folder", bg="lightgreen", command = remove_folder).grid(row = 65, column =2)
Button(root, text = "List all Files in Directory", bg="lightgreen", command = list_files).grid(row = 85,column = 2)
root.mainloop()


