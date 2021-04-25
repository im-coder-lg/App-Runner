import tkinter as tk
from tkinter import filedialog, Text
import os


#Root
root=tk.Tk()
apps=[]

#AddApp command definition
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()




    filename=filedialog.askopenfilename(initialdir="/", title="Choose ya file, mate!", filetypes=(("executables","*.exe"),("all.files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label=tk.Label(frame, text=app, bg="gray")
        label.pack()



def runApps():
    for app in apps:
        os.startfile(app)

#Canvas
canvas=tk.Canvas(root, height=500, width=500, bg="#bbb2e9")
canvas.pack()

frame=tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)



#Button
openFile=tk.Button(root, text="Open File", padx=10, pady=5, fg="black", bg="#bbb2e9", command=addApp)
openFile.pack()

RunApps=tk.Button(root, text="Run Apps", padx=10, pady=5, fg="black", bg="#bbb2e9", command=runApps)
RunApps.pack()






#Mainloop
root.mainloop()

with open('appsave.txt', 'w') as f:
    for apps in apps:
        f.write(app + ',')





