n=input()
for i in range(n):
	list1 = [abs(int(x)) for x in raw_input().split(" ")]
	count = 0
	while list1[0]!=0 and list1[1]!=0:
		if list1[0]<list1[1]:
			list1[1]-=1
		else:
			list1[0]-=1
		count+=1
	print count+1
