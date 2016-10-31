def retrieveFile():
	try:
		bestStudent={}
		bestStudentStr= "The students ranks are as follows \n"

		fin = open("student.txt","r")
	except(IOError),e:
		print "File not found",e
	else:
		for line in fin:
			name,grade = line.split()
			bestStudent[grade] = name
		fin.close()

		for i in sorted(bestStudent.keys()):
			print bestStudent[i] + " Scored a " + i
			bestStudentStr += bestStudent[i]+ " scored a "+ i + "\n"
		print "\n"

	print bestStudentStr 

	fout = open("studentrank.txt","w")
	fout.write(bestStudentStr)
	fout.close()


def main():
	retrieveFile()
if __name__ == "__main__":
	main()

