n=input()
list1=[]
temp=1
for i in range(n):
    list1.append([int(x) for x in raw_input().split(" ")])
for i in range(n):
    if i!=n-1 and temp!=0:
        if list1[i][0]>list1[i+1][0] and list1[i][1]<list1[i+1][1]:
            print "Happy Alex"
            temp=0
        elif list1[i][0]<list1[i+1][0] and list1[i][1]>list1[i+1][1]:
            print "Happy Alex"
            temp=0
    else:
        break
if temp==1 and n<100:
	for i in range(n):
		if i!=n-1 and temp!=0:
			for j in range(i+1,n):
				if temp!=0:
					if list1[i][0]>list1[j][0] and list1[i][1]<list1[j][1]:
						print "Happy Alex"
						temp=0
					elif list1[i][0]<list1[j][0] and list1[i][1]>list1[j][1]:
						print "Happy Alex"
						temp=0
				else:
					break
		else:
			break
if temp==1:
	print "Poor Alex"