import tkinter as tk
from tkinter import filedialog, Text
import os


#Root
root=tk.Tk()

#AddApp command definition
def addApp():
    filename=filedialog.askopenfilename(initialdir="/", title="Choose ya file, mate!", filetypes=(("executables","*.exe"),("all.files", "*.*")))


#Canvas
canvas=tk.Canvas(root, height=500, width=500, bg="#bbb2e9")
canvas.pack()

frame=tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)



#Button
openFile=tk.Button(root, text="Open File", padx=10, pady=5, fg="black", bg="#bbb2e9", command=addApp)
openFile.pack()

RunApps=tk.Button(root, text="Run Apps", padx=10, pady=5, fg="black", bg="#bbb2e9")
RunApps.pack()





#Mainloop
root.mainloop()
