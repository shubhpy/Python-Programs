from Tkinter import *
import tkMessageBox

def openGrades():
	f1= open("studentsgrades.txt")
	aboutStudents.delete(1.0, END)
	StudentsGradeStr=""
	for i in f1:
		StudentsGradeStr += i
	aboutStudents.insert(END , StudentsGradeStr)
	f1.close()
	return


def openRanks():
	f2= open("studentsranks.txt")
	aboutStudents.delete(1.0, END)
	StudentsRankStr=""
	for i in f2:
		StudentsRankStr += i
	aboutStudents.insert(END, StudentsRankStr)
	f2.close()
	return


def openfiles(selection):
	if selection=="Students Grades":
		openGrades()
	else:
		openRanks()
	return

def aboutMe():
	tkMessageBox.showinfo("U r trolled!", "yes you are")
	return

def buttoncmd():
	updategrades = aboutStudents.get(1.0,END)
	fo=open("studentsgrades.txt","w")
	fo.write(updategrades)
	fo.close()
	return

app = Tk()
app.title("GUI Ex 2")
app.geometry("600x500+200+200")

menubar = Menu(app)

filemenu  = Menu(menubar,tearoff=0)
filemenu.add_command(label="Open Grades" , command=openGrades)
filemenu.add_command(label="Open Ranks" , command=openRanks)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=app.quit)
menubar.add_cascade(label="File",menu=filemenu)

helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label="About Me",command=aboutMe)
menubar.add_cascade(label="Help",menu=helpmenu)

app.config(menu=menubar)

aboutStudents=Text(app)
aboutStudents.insert(END, "Choose students information above ")
aboutStudents.pack()

studFiles= StringVar()
studFiles.set(None)
files=["Students Grades","Student Ranks"]
studDropDown = OptionMenu(app,studFiles,*files,command=openfiles)
studDropDown.pack()

button = Button(app,text="Save Grades",width=20,command=buttoncmd)
button.pack(side="bottom",padx=15,pady=15)

app.mainloop()