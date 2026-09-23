'''
Usage of super()

class Father:
    """Father class with base fproperty argument"""
    def __init__(self,fproperty):
        self.fproperty = fproperty
    def father_property(self):
        print(f"Father's property is {self.fproperty}")
class Son(Father):
    """son started earning"""
    def __init__(self,sproperty,fproperty):
        super().__init__(fproperty)
        self.sproperty = sproperty      
    def son_property(self):
        print(f"Son's property is {self.sproperty}")
        print(f"Father's and Son's together property is {self.sproperty + self.fproperty}")
o1 = Son(600000,400000)
o1.father_property()
o1.son_property()
Method overrding => callinh superclass method

super().method()

#Calculating thae areas of Square,Rectanglr

class Square:
    """Area of Square"""
    def __init__(self,a):
        self.a = a
    def area(self):
        print( f"Area of sqaure is {self.a * self.a}")
class Rectangle(Square):
    """Derived Class"""
    def __init__(self,a,b):
        self.b = b
        super().__init__(a) #calling superclass constructor with args
    def area(self):
        super().area() #Calling superclass method
        print( f"Area of rectangle is {self.a * self.b}")
        #super().area()
o1 = Rectangle(5,2)
print(o1.area())
a,b = map(int,input("Enter values: ").split(","))
o2 = Rectangle(a,b)
o2.area()
##o2 = Square(4)
##print(o2.area())


Multiple Inheritance => Whatsapp scenario => Users, Premium Users, Business Users
Multiple base class is derived from multiple base classes

class base_cls1:
    statements-----------
    ---------------------
    ---------------------
    ---------------------
    ---------------------
class base_cls2:
    statements-----------
    ---------------------
    ---------------------
    ---------------------
    ---------------------
class derived_clas(base_cls1,base_cls2):
    statements-----------
    ---------------------
    ---------------------
    ---------------------
    ---------------------   

class Users:
    """Users class with basic features"""
    def voice_call(self):
        print("User can make voice call")
class Notifications:
    """Notifications reaching out"""
    def send_notifications(self):
        print("Uswer can get otifications")
class PremimunUsers(Users,Notifications):
    """Extra featuree added"""
    def vefication_badge(self):
        print("User is verified and blueticks added")
u1 = PremimunUsers()
u1.vefication_badge()
u1.voice_call()
print(dir(u1))

Multilevel Inheritance => Level by Level
class base_cls1:
    statements-----------
    ---------------------
    ---------------------
    ---------------------
    ---------------------
class base_cls2(base_cls1):
    statements-----------
    ---------------------
    ---------------------
    ---------------------
    ---------------------
class base_cls3(base_cls2):
    statements-----------
    ---------------------
    ---------------------
    ---------------------
    ---------------------   


class Users:
    """Users class with basic features"""
    def send_messages(self):
        print("User can send messages")
    def voice_call(self):
        print("User can make voice call")
class Business_User(Users):
    """First derived class"""
    def create_catalog(self):
        print("Details added sucessfully")
class premimumUsers(Business_User):
    """second derived class"""
    def vefication_badge(self):
        print("User is verified and blueticks added")
u1 = premimumUsers()
u1.vefication_badge()
u1.send_messages()
u1.create_catalog()
u1.voice_call()
''' 
class CSE:
    """the base class"""
    def students_total(self):
        print("Total number of students are 100")
class Section_A(CSE):
    def total_in_seta(self):
        print("Total number of students are 50")
class Section_B(CSE):
    def total_in_setb(self):
        print("Total number of students are 25")
class Section_C(CSE):
    def total_in_setc(self):
        super().students_total()
        print("Total number of students are 25")

s1 = Section_C()
s1.total_in_setc()


