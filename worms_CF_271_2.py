n=input()
listn=[int(x) for x in raw_input().split(" ")]
m=input()
list_label=[int(x) for x in raw_input().split(" ")]
list1=[0]
for i in listn:
	list1.append(i+list1[-1])
list1.remove(0)
def send(N,list2,ind):
	a=len(list2)
	if a==1:
		if N<=list2[0]:
			print ind
		else:
			print ind+1
	elif N<list2[a/2]:
		send(N,list2[0:a/2],ind/2)
	else:
		send(N,list2[a/2:a+1],ind)
for j in list_label:
	send(j,list1,n/2)