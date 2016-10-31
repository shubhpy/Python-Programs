n,k = [int(x) for x in raw_input().split(" ")]
list3=[n]
list1=[]
def divOf(z):
	global list1
	if z==1:
		list1.append(1)
	elif z==2 or z==3:
		list1.append(1)
		list1.append(z)
	else:
		list1.append(1)
		for j in range(2,(z/2)+1):
			if z%j==0:
				list1.append(j)
				if len(list1)>10000000:
					break
		list1.append(z)
def divList(list2):
	global list1
	for i in list2:
		if i>=963761198400:
			i=i/10000
			divOf(i)
			if len(list1)>100000:
				break
		else:
			divOf(i)
			if len(list1)>100000:
				break
if k>=100000:
	for i in range(100000):
		divList(list3)
		list3=list1[:]
		list1=[]
else:
	for i in range(k):
		divList(list3)
		if len(list1)>100000:
			break
		else:
			list3=list1[:]
			list1=[]
for i in list3:
	print i,