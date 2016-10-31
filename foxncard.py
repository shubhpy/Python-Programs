n=int(raw_input())
list1=[]
list2=[]
m=0
for i in range(0,n):
    list1.append([int(x) for x in raw_input().split(' ')])
    m=m+list1[i][0]
print list2
print list1
for i in range(n):
    list2.append(j for j in list1)
for i in range(n):
    list1[i].reverse()
c=j=m=0
for j in range(1,m+1):
    if j%2!=0:
        i=list2.index(max(list2))
        mx=max(max(list2))
        c=+mx
        list2[i].remove(mx)
        list1[len(list1)-1-i].remove(mx)
        print list2
        print list1
    else:
        k=list1.index(min(list1))
        mn=max(max(list1))
        j+=mn
        list1[k].remove(mn)
        list2[len(list2)-1-k].remove(mn)
        print list2
        print list1
print c,j
print list2
print list1
