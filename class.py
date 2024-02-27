#insatnce method
"""class A:
    def f1(self):
        self.a=5
    def f2(self,x,y):
        self.b=x
        self.b=y
obj1=A()
A.f1(obj1)
print(obj1.a)"""
#static method
"""class A:
    @staticmethod
    def f1():
        print("Hello Avaneesh")
    @staticmethod
    def f2(a,b):
        print(a,b)
A.f1()
A.f2(2,3)"""
#class method
"""class B:
    @classmethod
    def f1(cls):
        cls.x=10
obj1=B()
obj1.f1()
print(B.__dict__)"""
#Problem 1
"""class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
obj1=Person("Avaneesh",20)
obj2=Person("Amar",30)
obj3=Person("Adarsh",29)
obj2.show()
obj1.show() 
obj3.show()
obj4=Person("Arpit",29)   
obj4.show()"""
#problem 2
"""class Circle:
    def __init__(self,radius=0):
        self.radius=radius
    def set_radius(self,radius):
        self.radius=radius
    def get_radius(self):
        return self.radius
    def get_Area(self):
        return 3.14*self.radius**2
    def getCircumference(self):
        return 2*3.14*self.radius
r=Circle()
r.set_radius(4)   
r.get_radius()
print(r.get_radius())
print(r.get_Area())
print(r.getCircumference())
r.get_Area()
r.getCircumference()"""
#problem 3
"""class Javatpoint:  
    def __init__(self):  
        self.emp = "None"  
    def getEmp(self):  
        return self.emp  
    def setEmp(self, emp):  
        self.emp = emp  
Avaneesh = Javatpoint()  
Adarsh = Javatpoint()  
Amar = Javatpoint()
Amar.setEmp("Software Developer")   
Avaneesh.setEmp("Frontend Developer")  
Adarsh.setEmp("Backend Developer")  
print(Avaneesh.emp)  
print(Adarsh.emp) 
print(Amar.emp)"""
#problem 4
"""class Rectangle:
    def __init__(self,lenght=0,width=0):
        self.length=lenght
        self.width=width
    def set_Dimensions(self,length,width):
        self.length=length
        self.width=width
    def showDimensions(self):
        return self.length,self.width
    def getArea(self):
        return self.length*self.width
Room=Rectangle()
Room.set_Dimensions(4,5)
print(Room.showDimensions())
print("Area of Room is:",Room.getArea())"""
#problem 5
class Book:
    def __init__(self,bookid,title,price):
        self.bookid=bookid
        self.title=title
        self.price=price
    def show(self):
        print(self.bookid,self.price,self.title)
Python=Book(1,"Brokenheart",500)
Python.show()