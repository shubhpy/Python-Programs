class Greeting(object):

	def __init__ (self,name):
    	pass
    def SayHello(self):
        print "Hello", self.__greeter
    def setgreeter(self, newname):
    	self.__greeter = newname
    	return
    def getgreeter(self):
    	return self.__greeter
s = Greeting("shubh")
s.setgreeter("vinay")
print s.getgreeter()