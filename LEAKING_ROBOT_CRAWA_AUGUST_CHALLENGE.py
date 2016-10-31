n=input()
for i in range(n):
	temp=1
	x,y = [int(x) for x in raw_input().split(" ")]
	temp=1
	if x<0 and x%2==0:
		if y<=abs(x) and y>=x:
			print "YES"
			temp=0
	if temp!=0:
		if x>0 and x%2!=0:
			if y<=x+1 and y>=(-x+1):
				print "YES"
				temp=0
	if temp!=0:
		if y>0 and y%2==0:
			if x>=(-y) and x<=(y-1):
				print "YES"
				temp=0
	if temp!=0:
		if y<0 and y%2==0:
			if x>=y and x<=(abs(y)+1):
				print "YES"
	if temp==1:
		if x==0 and y==0:
			print "YES"
		else:
			print "NO"