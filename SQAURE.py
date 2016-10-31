import math
x1,y1,x2,y2 = [int(x) for x in raw_input().split(" ")]
l=math.sqrt(pow((x1-x2),2) + pow((y1-y2),2))
if x1==x2:
	x3=x1+int(l)
	y3=y1
	x4=x2+int(l)
	y4=y2
	print x3,y3,x4,y4
elif y1==y2:
	x3=x1
	y3=y1+int(l)
	x4=x2
	y4=y2+int(l)
	print x3,y3,x4,y4
elif x1==y1 and x2==y2:
	x3=x2
	y3=y1
	x4=x1
	y4=y2
	print x3,y3,x4,y4
else:
	print -1
