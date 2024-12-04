#subscribing
print("Thanmai"[6]) #will print i last charater in the string
print("Thanmai"[-1]) #will print i last charater in the string
print(type(123)) #here 123 is int not string
print(type(100+200)) #gives integer
#print("123"+100)#TypeError: can only concatenate str (not "int") to str
#So we here "123" is considered as string and we cannot add int to a string thats y we get TypeError
print("123"+"456") #output is 123456 here + is concadination operation not addition operator
#print(123456[0])#TypeError: 'int' object is not subscriptable
#print(len(1234567)) #TypeError: object of type 'int' has no len() length is function potato machine is given a stone
#integer is whole numbers including negitive
print(type("thnamai"))#Type function helps in knwoing the datatype type checking
print(type(123))#<class 'int'>
print(type(3.123))#<class 'float'>
print(type(True))#<class 'bool'> here python will not recognice true as boolean only True is boolen same case with False
print(type("hello"))#<class 'str'>
#How to convert one data type to another in python it is called type casting
print(int("123")+int("100")) # output: 223 here we are converting str values into int using int fucntion this is type casting
#Type casting cannot be done on all types like
print(int(False))#output is '0'
print(int(True))#output is '1'
print(int(3.5678788))#output is '3'
#But
#print(int("abc")+123)#ValueError: invalid literal for int() with base 10: 'abc'
#print("Number of letters in your name:"+len(input("Enter your name")))#TypeError: can only concatenate str (not "int") to str
print("Number of letters in your name:"+str(len(input("Enter your name"))))#here str cannot be added with int
print(123+len(input("Enter your name")))#output is 130 123+7