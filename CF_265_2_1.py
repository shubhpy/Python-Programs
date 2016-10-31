n=input()
s1=raw_input()
s2=""
s3=""
temp=0
count=0
for i in range(n-1,-1,-1):
	s2+=s1[i]
for j in range(n):
	if temp==0:
		if s2[n-1-j]=="1":
			s3+="0"
		else:
			s3+="1"
			temp=1
	else:
		s3+=s2[n-1-j]
for k in range(n):
	if s1[k]!=s3[k]:
		count+=1
print count