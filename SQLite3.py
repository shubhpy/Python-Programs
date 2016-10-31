import sqlite3

createDb = sqlite3.connect(":memory:")

QCurs = createDb.cursor()

def createTable():
	QCurs.execute('''CREATE TABLE customers 
	(id INTEGER PRIMARY KEY, name TEXT, street TEXT, zip REAL)''')
 
def addCust(name,street,zip):
	QCurs.execute('''INSERT INTO customers (name,street,zip) 
	VALUES(?,?,?)''',(name,street,zip))


def main():

	createTable()

	addCust("shubh","DG",478)
	addCust("hubh","DaG",4785)
	addCust("subh","DsG",4783)
	addCust("shbh","DGd",4782)
	addCust("shub","DGf",4178)

	createDb.commit()

	QCurs.execute('SELECT * FROM customers ORDER BY zip')

	QCurs.execute('ALTER TABLE customers ADD COLUMN email TEXT')

	QCurs.execute('UPDATE customers SET email="shubh1910@gmail.com" WHERE id=1')	

	QCurs.execute('DELETE FROM customers WHERE id=2')

	QCurs.execute('SELECT * FROM customers ORDER BY id DESC')

	Labels = ["serial no","Name","Pata","Zip","EMAIL"]
	k=0

	for i in QCurs:
		print "\n"
		for j in i:
			print Labels[k],
			print j
			if k==4:
				k=0
			else:
				k+=1
			
	QCurs.close()

if __name__== "__main__": main()