'''
OOP - OBJECT ORIENTED PROGRAMMING - Objects
POP - Procedure Oriented Programming - Functions
A class is a blueprint of a object

A object is a real  world entity which contains - attributes(variables)
                                                 - methods(functions)
class is defined using class keyword
feature of oop - Encapuslation,Inheritance,Polymorphism

class Classname:
    """doc string"""
    #attributes - define data
    -------------------
    -------------------
    -------------------
    def f_name(self): #behaviour
    def __init__(self):
        -------------------
        -----function------
        -------------------
obj = ClassName()

#creating a student class

class Students:
    """Student details"""
    name = "meghana"
    age = 21
    place = "vizag"
    def details(self):
        print(f"{self.name} of age {self.age} is in {self.place}")
#Creating object
obj = Students()
print(obj)
print(dir(obj))
print(obj.name,obj.age,obj.place)
#print(obj.details())#type error
#print(obj.details()) #name error we have self but no reference
obj.details()
obj2 = Students()
obj2.details()

#In the above case haow may objesta are created the result is same
class Students:
    """Multiple Student details"""
    def details(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    #Accessing details
    def display(self):
        print(f"Student name is {self.name}")
        print(f"Student age is {self.age}, lives in {self.place}")
s1 = Students()
s1.details("vikram",32,"delhi")
s1.display()
##print(s1.__class__)
##print(s1.__doc__)
##print(s1.__dict__)
s2 = Students()
s2.details("meghana",21,"vizag")
s2.display()
s2 = Students()

#Here we want object to be initilized -> __init__
class Students:
    """Multiple Student details"""
    def __init__(self,name,age,place):
        self.name = name #instance variables
        self.age = age
        self.place = place
    #Accessing details
    def display(self): #instance method
        print(f"Student name is {self.name}")
        print(f"Student age is {self.age}, lives in {self.place}")
s1 = Students("meghana",21,"vizag")
s1.display()
s2 = Students("vikram",32,"delhi")
s2.display()

#Create a cars class with attributes as brand,name,price
#create multiple objects
class Cars:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def Car_details(self):
        print(f"Car company is {self.brand}")
        print(f"Car model is {self.name}")
        print(f"car price is {self.price}")
        print("="*25)
c1 = Cars("Mahindra","Thar",3000000)
c1.Car_details()
c2 = Cars("Suzuki","Baleno",600000)
c2.Car_details()

#Encapsulation - How the methods are binded to single class
#ins= similar way how we can assess data -> public,private,protected,private
#public attributes -> can be created and modified even outside class
class User:
    """usage of public attributes"""
    def __init__(self,username):
        self.user = username #public attribute
    def display(self):
        print(f"username is {self.user}")
u1 = User("Abhi")
print(u1.user)
u1.user = "Vikram" #We can modify the public attribute outsie the class
u1.display()

#protected attribute -> these can also be modified outside the class,it's mainly used as a hint/coding convetion for other developers/users
#to create a protected attribute as underscore - ex:- _otp
        
class User:
    """usage of protected attributes"""
    def __init__(self,username,_otp):
        self.user = username #public attribute
        self._otp = _otp #protectes attribute
    def display(self):
        print(f"username is {self.user}")
        print(f"your otp is {self._otp}")
u1 = User("meghana",3456)
u1.display()
u1._otp = 1429
u1.display()

#private attribute -> Restric the usage and cannot be directly accessed, we have the notation as double leading underscore(__pssword)
class User:
    """usage of private attributes"""
    def __init__(self,username,_otp,__password):
        self.user = username #public attribute
        self._otp = _otp #protected attribute
        self.__password = __password #private attribute
    def display(self):
        print(f"username is {self.user}")
        print(f"your otp is {self._otp}")
u1 = User("Vikram",4291,"Vikki123")
print(u1.user,u1._otp)
#print(u1.__password)
#in above case password cannot be accessed directly we use NameMangling
print(u1._User__password)
'''
#usage of getter(),setter() methods

class User:
    """usage of private attributes"""
    def __init__(self,username,_otp,__password):
        self.user = username #public attribute
        self._otp = _otp #protected attribute
        self.__password = __password #private attribute
    #usage of getter() method or get()
    def get_password(self):
        """Getter method for password"""
        return "*******"
    #usage of setter()
    def set_password(self,new_password):
        if len(new_password) <6:
            return 'password length is not matching'
        else:
            self.__password = new_password
            return 'update password'
    def display(self):
        print(f"username is {self.user}")
        print(f"your otp is {self._otp}")
u1 = User("Vikram",4291,"Vikki123")
print(u1.get_password())
print(u1.set_password("1234"))
print(u1.set_password("vik123"))
print(u1.get_password())
print(u1.__dict__)






