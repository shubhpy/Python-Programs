#https://practice.geeksforgeeks.org/problems/smallest-distant-window/0

S = list(input())
s = set(S)
l = len(list(s))
p = len(S)
for i in range(l,p+1):
    f=0
    for j in range(0,p-i+1):
        temp = S[j:j+i]
        t = set(temp)
        if t==s:
            print(len(temp))
            f=1
            break
    if f==1:
        break
