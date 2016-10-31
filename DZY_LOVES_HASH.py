p,n = [int(x) for x in raw_input().split(" ")]
list1=[]
list2=[]
for i in range(0,n):
	list1.append(input())
for i in range(0,n):
	x=list1[i]%p
	if x in list2:
		print i+1
		break
	else:
		list2.append(x)
	if i==n-1:
		print -1
		break



