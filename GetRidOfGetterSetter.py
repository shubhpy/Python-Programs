class Animal(object):

	__name="no name"
	__owner="none"

	def __init__(self,**kvargs):
		self._attributes = kvargs
	def set_attributes(self,key,value):
		self._attributes[key]=value
		return
	def get_attributes(self,key):
		return self._attributes.get(key,None)
	def noise(self):
		print "errr"
		return
	def noise2(self):
		print "noise2wali"
		Animal.noise(self)
		return

class Dog(Animal):

	def __init__(self , **kvargs):
		super(Dog,self).__init__()
		self._attributes = kvargs

	def noise(self):
		print "woof woof"
		Animal.noise(self)
		return
	def noise2(self):
		print "bhau bhau"
		Animal.noise(self)
		return

class Cat(Animal):

	def __init__(self , **kvargs):
		super(Cat,self).__init__()
		self._attributes = kvargs

	def noise(self):
		print "meow"
		return
	def noise3(self):
		print "ofcat"
		return

class Dat(Dog,Cat):
	def __init__(self , **kvargs):
		super(Cat,self).__init__()
		self._attributes = kvargs

	def noise(self):
		print "i dont know"
		return  


def playwithanimal(Animal):
	Animal.noise()
	Animal.noise2()
	print (Animal.get_attributes("__name"))
	print (Animal.get_attributes("__owner"))
	Animal.set_attributes("clean","yessssssssssssssssss")

	print Animal.get_attributes("clean")

def main():
	jake = Dog(__name="jake",__owner="paul")
	sophie = Cat(__name="sophie",__owner="sue")
	japhie= Dat(__name="japhie",__owner="paulsue")
	playwithanimal(jake)
	playwithanimal(sophie)
	playwithanimal(japhie)
	japhie.noise()

	print sophie.__class__
	print sophie.__dict__
	print Cat.__bases__

if __name__ == "__main__":
	main()