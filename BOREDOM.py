n=input()
list1=[int(x) for x in raw_input().split(" ")]
list1.sort()
Count=0
def Repeat(list1):
	global Count
	CLast=1
	CSecLast=1
	Last=list1[-1]
	for i in range(len(list1)-2,-1,-1):
		if list1[i]==Last:
			CLast+=1
		else:
			break
	SecLast=list1[i]
	if i==1:
		k=0
		SecSecLast=list1[k]
	elif i>1:
		for k in range(i-2,-1,-1):
			if list1[i]==SecLast:
				CSecLast+=1
			else:
				break
		SecSecLast=list1[k]
	if CLast>=CSecLast:
		list1.remove(Last)
		for j in range(CSecLast):
			list1.remove(SecLast)
		Count+=Last
	else:
		list1.remove(SecLast)
		for j in range(CLast):
			list1.remove(Last)
			list1.remove(SecSecLast)
		Count+=SecLast
	if list1!=[] and list1[0]==list1[-1]:
		Count+=(list1[0]*len(list1))
		print Count
	elif list1!=[] and list1[0]!=list1[-1]:
		Repeat(list1)
	else:
		print Count
Repeat(list1)