a1,a2,a3=[int(x) for x in raw_input().split(" ")]
b1,b2,b3=[int(x) for x in raw_input().split(" ")]
n=input()

if (a1+a2+a3)%5 >0:
	n=n-1-((a1+a2+a3)/5)
else:
	n=n-((a1+a2+a3)/5)

if (b1+b2+b3)%10 >0:
	n=n-1-((b1+b2+b3)/10)
else:
	n=n-((b1+b2+b3)/10)

if n>=0:
	print "YES"
else:
	print "NO"