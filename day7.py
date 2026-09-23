''' 
Inheritance => It is one of the key properties of OOP
We can acquire properties (features) from one class to another class
Types of Inheritance
- Single Inheritance -- Finger print -- One child class inheriting properties from single parent class
- Multiple Inheritance -- parent -> kids -- One child class can take properties from multiple parents
- Multilevel Inheritance -- level by level -- Famil tree
- Hierarchial Inheritance -- Multiple child classes inheriting from one parent class
- Hybrid Inheritance -- It's combination of different types of inheritance

SINGLE INHERITANCE
Parent class -  Base class
Child class - Derived class

class Base_class:
    statements--------
    ------------------
    ------------------
    ------------------
class  Derived_class(Base_class):
    statements--------
    ------------------
    ------------------
    ------------------
#updating user names in a profile page
class Users:
    """User class with basic details"""
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def fullname(self):
        return f'{self.fname + self.lname}'
#u1 = Users("meghana","vaddi")
#print(u1.fullname())
#Extending features by updating username
class update_users(Users):
    def update(self):
        return f'{self.fname.title().strip() +" "+ self.lname.title().strip()}'
#u1 = update_users('vikram','adithya')
#print(u1.fullname())
u1 = update_users(' vikram ',' aditya ')
print(u1.fullname())
print(u1.update())


#usage of class attribute and classmethod in Inheritance
#Class attributes - They can be accessed directly with classname
# class method - @classmethod

#banking senerio -- RBI Bank(Base Class) --> SBI,ICICI
class RBI:
    """Base class with amount"""
    cash = 10000000 #class attribute
    @classmethod
    def rbi_cash(cls):
        return f"available cash with RBI is {RBI.cash}"
b1 = RBI()
#print(b1.cash)
#print(b1.rbi_cash())
#print(RBI.cash) #We can also access directly using classname 
#print(RBI.rbi_cash())
class SBI(RBI):
    pass
##b1 = SBI()
##print(b1.rbi_cash())

class ICICI(RBI):
    cash = 5000000
    @classmethod
    def icici_cash(cls):
        print(f"ICICI cash is {cls.cash}")
        print(f"Total accessible cash is {cls.cash + cls.cash}")
b1 = ICICI()
print(b1.cash)
print(b1.rbi_cash())
b1.icici_cash()

#the same name we will access with classname 
class ICICI(RBI):
    cash = 5000000
    @classmethod
    def icici_cash(cls):
        print(f"ICICI cash is {cls.cash}")
        print(f"Total accessible cash is {cls.cash + RBI.cash}")
b1 = ICICI()
print(b1.cash)
b1.icici_cash()
print(b1.rbi_cash())
#Takeway -- if same classes is having same names as class attributres to access them we will use class names as RBI.cash,HDFC.cash

#In the same way what if we have different class attributes
class RBI:
    """Base class with amount"""
    amount = 10000000 #class attribute
    @classmethod
    def rbi_cash(cls):
        return f"available cash with RBI is {RBI.amount}"
b1 = RBI()
class SBI(RBI):
    pass
class ICICI(RBI):
    cash = 5000000
    @classmethod
    def icici_cash(cls):
        print(f"ICICI cash is {cls.cash}")
        print(f"Total accessible cash is {cls.cash + RBI.amount}")
b1 = ICICI()
print(b1.cash)
print(b1.amount)
b1.icici_cash()
print(b1.rbi_cash())


#Single Inheritance usage -- base class and derived class with constructor
#Kid,Father -- propertty secnerio

class Father:
    """Father class with base property amount"""
    def __init__(self):
        self.property = 25000000
    def father_property(self):
        print(f"Father's property is {self.property}")
##o1 = Father()
##o1.father_property()
    
class Son(Father):
    pass
o1 = Son()
print(o1.property)
o1.father_property()
#In above case its as it is not change in method and attribute usage

class Son(Father):
    """son started earning"""
    def __init__(self):
        self.property = 50000000
    def son_property(self):
        print(f"Son's property is {self.property}")
        print(f"Father's and Son's together property is {self.property + self.property}")
o1 = Son()
o1.father_property()
o1.son_property()
#In this case Constructor Overridingas parent and child classes is having
#Constructor child calss Constructor will override parent class Constructor
#we have usage of super()
#super class constructor --> super.__init__
# super class Constructor with args --> super__init__(args)
#superclass method(Method Overriding) --> super().method()
'''
class Father:
    """Father class with base property amount"""
    def __init__(self):
        self.property = 25000000
    def father_property(self):
        print(f"Father's property is {self.property}")
class Son(Father):
    """son started earning"""

    def __init__(self):
        super().__init__()
        self.sproperty = 5000000
        
    def son_property(self):
        print(f"Son's property is {self.sproperty}")
        print(f"Father's and Son's together property is {self.sproperty + self.property}")
o1 = Son()
o1.father_property()
o1.son_property()













    
