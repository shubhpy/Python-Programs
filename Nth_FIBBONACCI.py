import math
n,m=[int(x) for x in raw_input().split(" ")]
listA=[int(x) for x in raw_input().split(" ")]
listM=[]
for i in range(m):
	listM.append([int(x) for x in raw_input().split(" ")])
sum=0
Phi=(1+math.sqrt(5))/2.0
phi=(1-math.sqrt(5))/2.0
diff=Phi-phi

def NthFib(x):
	return int((math.pow(Phi,x) - math.pow(phi,x))/diff)

for i in range(m):
	if listM[i][0]==1:
		for j in range(listM[i][1],listM[i][2]+1):
			listA[j-1]+=NthFib(j-listM[i][1]+1)
	else:
		for j in range(listM[i][1],listM[i][2]+1):
			sum +=  listA[j-1]
		print sum
		sum=0