try:
	list=[3,4,5,6]
	a=int(input("enter number"))
	print(list[a])
except:
	print("index is out of range")
else:
	print("sucessfully run")
finally:
	print("complete")