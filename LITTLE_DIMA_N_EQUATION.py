a,b,c=[int(x) for x in raw_input().split(" ")]
list1=[]
count=0
for i in range(1,90):
	x=(b*pow(i,a))+c
	s=0
	if x>0 and x<1000000000:
		for k in str(x):
			s+=int(k)
		if s==i:
			count+=1
			list1.append(x)
print count
for j in list1:
	print j,