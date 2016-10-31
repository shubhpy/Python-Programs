n=input()
list1=[int(x)-1 for x in raw_input().split(" ")]
b=len(list1)
count=1
list1.insert(0,0)
list1.append(0)
time=1
for i in range(b+2):
    if list1[i]==0 and time==1:
        oldIndx=i
        time=2
    elif list1[i]==0 and time==2:
        newindx=i
        for j in range(oldIndx+1,newindx):
            list1[j]-=1
        count+=1
        oldIndx=newindx
    if max(list1)==0:
        break
if b>count:
    print count
else:
    print b