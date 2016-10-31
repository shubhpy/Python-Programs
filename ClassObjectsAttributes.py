import math
class Vector2D():
	# this format is neccesory REMEMBER IT ^_^ o_O !
	 def __init__(self,x,y):
	 	self.x=x
	 	self.y=y

	 def __add__(self,other):
	 	return Vector2D(self.x + other.x,self.y+other.y)

	 def __iadd__(self,other):
	 	self.x+=other.x
	 	self.y+=other.y
	 	return self

	 def __sub__(self,other):
	 	return Vector2D(self.x-other.x,self.y-other.y)

	 def __isub__(self,other):
	 	self.x-=other.x
	 	self.y-=other.y
	 	return self

	 def __imul__(self,other):
	 	self.x*=other.x
	 	self.y*=other.y
	 	return self

	 def __idiv__(self,other):
	 	self.x/=float(other.x)
	 	self.y/=float(other.y)
	 	return self

	 def __div__(self,other):
	 	return Vector2D(self.x/float(other.x),float(self.y)/other.y)

	 def getlength(self):
	 	return math.sqrt(self.x**2 + self.y**2)

	 def normalized(self):
	 	length = self.getlength()
	 	return length

	 def getangle(self):
	 	return math.degrees(math.atan2(self.x,self.y))

# to print object like a string
	 def __str__(self):
	 	return "x: " + str(self.x) +", Y: " + str(self.y)

def main():
	vec = Vector2D(5,6)
	vec2 = Vector2D(2,3)

	print vec
	print vec2

# METHOD OBJECT

	tempmethod = vec.getangle

	vec = vec  + vec2
	print vec

	vec = vec  - vec2
	print vec

	vec += vec2
	print vec

	vec *= vec2
	print vec

	vec -= vec2
	print vec

	vec /= vec2
	print vec

	vec =vec/vec2
	print vec

	vec +=Vector2D(9,6)
	print vec

	print vec.normalized()
	print vec.getangle()

# when we declared the method object it got the
# vec of that time and even when we had changed vec then the tempmethod was also changed
# so BE AWARE OF IT
	print tempmethod()

	print vec.getlength()

if __name__=="__main__":
	main()