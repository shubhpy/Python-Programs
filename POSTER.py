n,k = [int(x) for x in raw_input().split(" ")]
str=raw_input()
if n-k<k:
	for i in range(n-k):
		print "RIGHT"
	for i in range(n):
		print "PRINT "+ str[-1-i]
		if i!=n-1:
			print "LEFT"
else:
	for i in range(k-1):
		print "LEFT"
	for i in range(n):
		print "PRINT "+ str[i]
		if i!=n-1:
			print "RIGHT"