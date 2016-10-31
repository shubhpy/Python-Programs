s = raw_input()
k= input()
y=1
res=0
list1 = [int(i) for i in raw_input().split(" ")]
m=max(list1)
sl = len(s)
abcd=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for x in s:
	ix=abcd.index(x)
	res = res + (y*list1[ix])
	y += 1
for x in range(0,k):
	res = res + (sl+1+x)*m
print res