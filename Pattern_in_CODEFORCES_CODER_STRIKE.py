n=input()
list1=[]
for i in range(n):
	list1.append(raw_input())
for j in range(len(list1[0])):
	for i in range(n):
		if list1[i][j]!="?":
			
