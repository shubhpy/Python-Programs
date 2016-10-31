t=input()
list2=[]
for j in range(t):
	n,k = [int(x) for x in raw_input().split(" ")]
	list1=[int(x) for x in raw_input().split(" ")]
	count=0
	for i in list1:
		if k==0:
			break
		if i%2==0:
			count+=1
		if count==k:
			break
	if k!=0:
		if count>=k:
			print "YES"
		else:
			print "NO"
	else:
		print "NO"