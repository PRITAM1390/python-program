#creating a function without parameters
def func1():
	print("hi")
	print("hello")
func1()

#with  parameters
def func2(a): #a=1
	print("hi\t",a)
func2("abs")

#with 2/3 parameters
def func3(a,b,c): #a=2,b=5,c=6
	d=a+b+c
	print(a,b,c,d)
func3(2,5,6)

#with default parmeters
def func4(university="CMR"):
	print("i am in "+"\t"+university)
func4("IIIM")
func4("IIIT")
func4()
#return statement
def func5(a,b,c): #a=2,b=5,c=6
	d=a+b+c
	return d
e=func5(2,5,6)
print(e)
#calling one function from other and return statement
def func6(a,b):
	print("hey other function")
	c=a+b
	return c
def func7():
	print("hello i am going to add another function")
	s=func6(2,7)
	print("addition is",s)
func7()

#sum of all elements of list
def func8(a,b,c,d,e,f,g):
	d=a+b+c+d+e+f+g
	print("d")
func8(2,3,4,5,6,7,7)