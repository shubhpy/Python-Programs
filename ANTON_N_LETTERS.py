list1=[x for x in raw_input().split(", ")]
list1.append(list1[0][1])
list1.remove(list1[0])
if len(list1)!=1:
	list1.append(list1[-2][0])
	list1.remove(list1[-3])
	l=len(list1)
	count=0
	i=0
	while len(list1)!=0:
		if list1==[]:
			break
		else:
			val=list1[i]
			countchar=list1.count(val)
			if countchar==1:
				count+=1
				list1.remove(val)
			else:
				count+=1
				for j in range(countchar):
					list1.remove(val)
	print count
elif list1[0]=="}":
	print 0
else:
	print 1