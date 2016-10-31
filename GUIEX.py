from Tkinter import *
import tkMessageBox

def beenClicked():
	radioValue = relStatus.get()
	tkMessageBox.showinfo("you clicked ",radioValue)
	return

def changeLabel():
	name="thanks for click " + yourName.get()
	labelText.set(name)
	yourName.delete(0, END)
	yourName.insert(0, "MY name is SHUbh")
	return

app = Tk()
app.title("GUI EXMAPLE")
app.geometry('450x300+200+200')

labelText = StringVar()
labelText.set("click button")
label1 = Label(app,textvariable=labelText,height=4)
label1.pack()

checkBoxVal = IntVar()
checkBox1 =Checkbutton(app,variable=checkBoxVal,text="Happy?")
checkBox1.pack()

custName = StringVar(None)
yourName= Entry(app,textvariable = custName)
yourName.pack()

relStatus = StringVar()
relStatus.set(None)
radio1 = Radiobutton(app,text="single", value="Single",variable=relStatus,command=beenClicked).pack()
radio1 = Radiobutton(app,text="married", value="Married",variable=relStatus,command=beenClicked).pack()

button1 = Button(app ,text="click here",width=20,command=changeLabel)
button1.pack(side='bottom',padx=15,pady=15)

app.mainloop()

