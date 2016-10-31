n,d= [int(x) for x in raw_input().split(" ")]
list1=[]
list1=[int(x) for x in raw_input().split(" ")]
sum=0
for i in range(n):
	sum += list1[i]
sum+= (n-1)*10
if sum>d:
	print -1
else:
	print ((n-1)*2)+((d-sum)/5)
