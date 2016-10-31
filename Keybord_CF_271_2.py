d=raw_input()
s=raw_input()
keyboard=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l",";","z","x","c","v","b","n","m",",",".","/"]
ans=""
if d=="R":
	for i in s:
		if i in ["a","q","z"]:
			ans=ans+i
		else:
			index=keyboard.index(i)
			ans=ans+keyboard[index-1]
	print ans
else:
	for i in s:
		if i in ["p",";","/"]:
			ans=ans+i
		else:
			index=keyboard.index(i)
			ans=ans+keyboard[index+1]
	print ans