n=input()
list1=[int(x) for x in raw_input().split(" ")]
count=1
num1=list1.count(1)
num=num1
for i in range(n):
	if list1[i]==1:
		num=num-1
		if i!=n-1:
			if list1[i+1]==1:
				count+=1
			elif num!=0:
				count+=2
if num1==0:
	print 0
else:
	print count