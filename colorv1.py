from tkinter import *
from random import randint

#-------------------------- main window --------------------------
root = Tk()
root.title("colorv1")
don = StringVar()


#-----------------------------------------------------------------

def fshow():
    try: 
        labmain["text"] = don.get()
        labmain["bg"] = don.get()
    except:
        labmain["text"] = "Aadil Say :-\nError"
        labmain["bg"] = "black"
        labmain["fg"] = "white"

def frand():
    code = labmain["bg"] = f"#{randint(0,0xffffff):06x}"
    labmain["text"] = code
    don.set(code)
#---------------------------------------------------------------------
lab0 = Label(root,width = 8,height = 2)
lab0.grid(row = 0,column = 0,sticky = "ewns")

labmain = Label(root,bg = "red",width = 20,height = 10,borderwidth=2, relief="solid")
labmain.grid(row = 1,column = 1,columnspan = 2,sticky = "ewns")

lab0 = Label(root,width = 8,height = 2)
lab0.grid(row = 0,column = 3,sticky = "ewns")

lab0 = Label(root,width = 8,height = 1)
lab0.grid(row = 2,column = 0,sticky = "ewns")

ent = Entry(root,textvariable = don)
ent.grid(row = 3,column = 1,columnspan = 2,sticky = "ewns")

lab0 = Label(root,width = 8,height = 1)
lab0.grid(row = 4,column = 0,sticky = "ewns")

bshow = Button(root,text = "SHOW",command = fshow)
bshow.grid(row = 5,column = 1,sticky = "ewns",columnspan = 2)

lab0 = Label(root,width = 8,height = 1)
lab0.grid(row = 6,column = 0,sticky = "ewns")

brand = Button(root,text = "RANDOM",command = frand)
brand.grid(row = 7,column = 1,sticky = "ewns",columnspan = 2)

lab0 = Label(root,width = 8,height = 2)
lab0.grid(row = 8,column = 0,sticky = "ewns")

don.set("Wellcome")
labmain["text"] = "Devloped By :-\nAadil Mugal"

#-------------------------------- event loop --------------------------
root.mainloop()