from string import Template
# 1
#saves time typing and reduces code length
#2
# like if u wbant to use the delimeter $ in the template 
# declaration then u can use double $$
#3
'''to attach a string at the end od the $item u'll have to use {} 
like "the ${place}yard is far away from here"
its output will be "the shipyard is far awat from here"
'''
def main():
	cart=[]
	cart.append(dict(item="coke",price=2,qty=1))
	cart.append(dict(item="cake",price=8,qty=1))
	cart.append(dict(item="joke",price=1,qty=1))

	print cart

	t = Template("$qty x $item = $price")
	total=0
	for data in cart:
		print t.substitute(data)
		total += data["price"]
	print "total = " ,total
if __name__ == "__main__":
	main()

