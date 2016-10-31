n,h = [int(x) for x in raw_input().split(" ")]
list1=[]
list1=[int(x) for x in raw_input().split(" ")]
hour=0
list1.sort()
while h!=1:
	hour += h*list1[0]
	list1.remove(list1[0])
	h-=1
	if list1==[]:
		break
for i in list1:
	hour += i
print hour