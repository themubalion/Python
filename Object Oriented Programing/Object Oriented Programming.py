# Object oriented programmming

class MyClass:

    # Here to note that we are not defining functions in the class we are defining the methods for the class.

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def add(self,x,y):
        return x + y

    def meow(self):
        print('meow')
    
    def getname(self):
        return self.name

    def getage(self):
        return self.age

# We can call the method by writing the variable that you defined as being in any class and then providing the method i.e -> variable.method(), you can also define the arguement of the method in class using def mehod(self,paremter), or you can use multiple perimeter seperated by the commas. i.e. --> def method (self,arguement1,arguement2). If you define multiple arguements filling all the arguements will be necessary.

# *** Init function is used to define the perimeter for the class.

c = MyClass('sufiyan',9)
# print(type(c))


c.name = "lily"
# print(c.name)

# c.meow()

# print(c.add(5,2))

me = MyClass('Mubashshir Ali',16)

# In the above code we are defining the method giving it the arguement of name and the age

print(me.getage())
print(me.getname())