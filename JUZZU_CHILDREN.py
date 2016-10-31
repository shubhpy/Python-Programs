n,m=[int(x) for x in raw_input().split(" ")]
list1=[int(x) for x in raw_input().split(" ")]
for i in range(n):
	list1[i]=[list1[i],i+1]
while len(list1)!=1:
	if list1[0][0]<=m:
		list1.remove(list1[0])
	else:
		list1.append([list1[0][0]-m,list1[0][1]])
		list1.remove(list1[0])
print list1[0][1]
