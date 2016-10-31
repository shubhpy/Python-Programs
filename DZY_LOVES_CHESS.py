n,m = [int(x) for x in raw_input().split(" ")]
list1=[]
list2=[]
for l in range(-(n*m),2*(n*m)):
	list2.append("*")
temp=0
for i in range(0,n):
	list1.append(raw_input())
for i in range(0,n):
	for j in range(0,m):
		if list1[i][j]==".":
			temp+=1
			if temp==1:
				list2[(i*m)+j]="B"
			else:
				if j==0:
					if list2[(i*m)+j+1]=="B" or list2[(i*m)+j+m]=="B" or list2[(i*m)+j-m]=="B":
						list2[(i*m)+j]="W"
					elif list2[(i*m)+j+1]=="W" or list2[(i*m)+j+m]=="W" or list2[(i*m)+j-m]=="W":
						list2[(i*m)+j]="B"
				elif list2[(i*m)+j-1]=="B" or list2[(i*m)+j+1]=="B" or list2[(i*m)+j+m]=="B" or list2[(i*m)+j-m]=="B":
					list2[(i*m)+j]="W"
				elif list2[(i*m)+j-1]=="W" or list2[(i*m)+j+1]=="W" or list2[(i*m)+j+m]=="W" or list2[(i*m)+j-m]=="W":
					list2[(i*m)+j]="B"
				else:
					list2[(i*m)+j]="B"
		else:
			list2[(i*m)+j]="-"
c=list2.count("*")
for l in range(0,c):
	list2.remove("*")
for i in range(0,n):
	strin=""
	for k in range(0,m):
		strin+=str(list2[(i*m)+k])
	print strin