import math
Phi=(1+math.sqrt(5))/2.0
phi=(1-math.sqrt(5))/2.0
diff=Phi-phi

def NthFib(x):
	return int((math.pow(Phi,x) - math.pow(phi,x))/diff)
print NthFib(6)