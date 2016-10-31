n,v = [int(x) for x in raw_input().split(" ")]
list2=[]
list1=[]
for i in range(n):
	list1.append([int(x) for x in raw_input().split(" ")])
count=0
for i in range(n):
	temp=0
	for j in list1[i]:
		if j!=list1[i][0]:
			if temp==1:
				break
			elif v>j:
				temp=1
				count+=1
				list2.append(i)
				break
print count
list2.sort()
for m in list2:
	print m,