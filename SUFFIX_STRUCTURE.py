s=raw_input()
t=raw_input()
temp=0
for i in t:
	if s.count(i)>=t.count(i):
		temp=1
	else:
		temp=0
		break
if temp==0:
	print "need tree"
else:
	print s