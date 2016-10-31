n=input()
list1=[int(x) for x in raw_input().split(" ")]
count=0
def f(l,r,x):
	sum=0
	for k in range(l,r+1):
		if list1[k-1]==x:
			sum+=1
	return sum

for j in range(1,n+1):
	for i in range(1,j):
		if f(1,i,list1[i-1])>f(j,n,list1[j-1]):
				count+=1
print count