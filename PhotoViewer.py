from tkinter import *
from PIL import ImageTk,Image
import glob
import os

root=Tk()
root.title("TITLE!")

directory="C:\\Users\\Shekhar Sharma\\Desktop\\New folder\\" #Enter folder directory HERE 


myList=os.listdir(directory)


print("Images detected are - \n")
for i in range(len(myList)):
    print(myList[i])
    myList[i]=ImageTk.PhotoImage(Image.open(directory+myList[i]))

my_label=Label(image=myList[0])
my_label.place(x=300,y=100)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.place_forget()
    my_label = Label(image=myList[image_number-1])
    button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))

    if image_number==len(myList):
        button_forward=Button(root,text=">>",state=DISABLED)

    my_label.place(x=225,y=125)
    button_back.place(x=200,y=600)
    button_forward.place(x=1100,y=600)

def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.place_forget()
    my_label = Label(image=myList[image_number-1])
    button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))

    if image_number==1:
        button_back=Button(root,text="<<", state=DISABLED)
    
    my_label.place(x=225,y=125)
    button_back.place(x=200,y=600)
    button_forward.place(x=1100,y=600)
    
button_back=Button(root,text="<<", command = lambda:back(2), state=DISABLED)

button_forward=Button(root,text=">>", command = lambda:forward(2))

button_back.place(x=200,y=600)
button_forward.place(x=1100,y=600)

root.mainloop()

