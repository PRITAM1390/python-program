class Test:
	h=0
	def my_fun(self,k):
		print("hii,i'm in the class")
		self.h=k #assigning the value to instance variable
		print(self.h)
o=Test() #creat object for class test
o1=Test()
o.my_fun(2)
o1.my_fun(4)
o3=Test()
print(o3.h)
