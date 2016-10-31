n,p=[int(x) for x in raw_input().split(" ")]
s=raw_input()
lists=[q for q in s]
ABCD=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list1=ABCD[0:p]

def palin(s1):
	N=len(s1)
	for j in range(N):
		if s1[j]!=s1[N-1-j]:
			return 0
	return 1

def sendstring(s2):
	for m in range(n-1):
		for l in range(m+2,n):
			if palin(s2[m:l])==1:
				return 1
	return 0
for i in range(n):
	ind=list1.index(lists[n-1-i])
	if ind==p-1:
		lists[n-1-i]=list1[0]
	else:
		work=lists[n-1-i]
		lists[n-1-i]=list1[ind+1]
		if sendstring(lists)==1:
			lists[n-1-i]=work
		else:
			break
print lists