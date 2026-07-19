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
    std_name = 'Meenakshi' #Class attribute

st_ = student()
print(st_)


Attributes:
- Attributes are the variables that belongs to an object or the class
    
'''

    
class how:
    def details(self, name, age):
        self.name = name  #instance attribute
        self.age = age
    def name(self):
        print(self.name)
s1_ = how()
s1_.details('Meenakshi',21)

print(f"Name: {s1_.name}\nAge: {s1_.age}")
