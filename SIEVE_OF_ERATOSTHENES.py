from math import sqrt
n=10000000
list1=[[int(x),1] for x in range(2,n+1)]
for i in range(2,int(sqrt(n))+1):
	if list1[i-2][1]==1:
		for k in range(n+1):
			if i*(i+k)<=n:
				list1[i*(i+k)-2][1]=0
			else:
				break
for i in list1:
	if i[1]==1:
		print i[0],