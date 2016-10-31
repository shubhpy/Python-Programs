import shelve
def addcust(database):

	boolean = "n"
	if boolean == "n":
		customers={}

	print "add customer now"

	custNum = raw_input("enter customer num : ")
	customers["Name"]= raw_input("enter customer Name : ")
	customers["zip"]= input("enter customer zip : ")
	database[custNum] = customers
	boolean = raw_input("want to store more (y/n) : ")
	print "\n"
	if boolean == "y":
		addcust(database)
	else:
		return

def main():
	database = shelve.open("customersinfo.dat",writeback=True)
	addcust(database)
	lukforCust = 1

	while (lukforCust!= 0):
		lukforCust = raw_input("enter customer num u want to show details of : ")
		if lukforCust == 0:
		 	break
		else:
			try:
		 		for i in database[lukforCust]:
		 			print i , " " , database[lukforCust][i]
		 		print "\n"
		 	except (KeyError) ,e :
		 		print "Can not found Customer with Num ", e
		 		break
	database.close()	

if __name__ == "__main__": 
	main()