
class Perform(object):
	#Switch case to select an operation to be perform
	def operates(self,choosen):
		method_name='operated_'+str(choosen)
		method=getattr(self,method_name,lambda:"***Invalid operation***")
		return method()
		
	def operated_1(self):
		return "Arithmatic"
		
	def operated_2(self):
		return "date"