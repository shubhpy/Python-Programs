f1,f2=[int(x) for x in raw_input().split(" ")]
n=input()

def fseq(i):
	if i==1:
		return f1
	elif i==2:
		return f2
	else:
		return fseq(i-1)-fseq(i-2)

print (fseq(n)%1000000007)