'''


                                        OOPS
                                        ----

--> Object-oriented programming System(oops), This will be organizes the code using classes and objects....

USES:
-Code reusable
-Easy maintaince
-Clear understanding
-Better security

Classes:
- It is a blue print or a template used to create an object..

class class_name:
    pass
    
Objects:
- Object is a instance of the class

class student:
    std_name = 'Maggi' #Class attribute

st_ = student()
print(st_)


Attributes:
- Attributes are the variables that belongs to an object or the class
    
'''
class how:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def nam(self):
        print(self.name)
s1 = how("Maggi",34)
print(s1.nam())

class calc:
    def add(self, num1, num2):
        print(num1 + num2)
    def sub(self, num1, num2):
        print(num1 - num2)
c = calc()
c.add(2,90)
c.sub(8, 9)
