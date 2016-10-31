n=input()
list1=[int(x) for x in raw_input().split(" ")]
mx=max(list1)
mn=min(list1)
if mx!=mn:
	mxC=list1.count(mx)
	mnC=list1.count(mn)
	print mx-mn,mxC*mnC
else:
	print 0,(n*(n-1))/2