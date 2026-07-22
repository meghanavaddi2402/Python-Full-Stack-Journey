'''
=> Polymorphism :-
- Polymorphism means many forms
- Polymorphism allows same method, function or operator
1.Method Overloading :-
- Method Overloading means having multiple methods with same name but differeent parameters
- Example :-

class cal:
    def add(self,a,b=0):
        print(a+b)
    def add(self,a,b=0,c=0):
        print(a+b+c)
o = cal()
o.add(2,4)
o.add(10,2,4)

2. Method Overriding :-
- Method Overriding occurs when a child claass provides it's own implementation of a method already defined in it's parents class

class animals:
    def sound(self):
        print("Animals make sounds")
class dog(animals):
    def sound(self):
        print("Dog barks")
d = dog()
d.sound()

3. Operator Overloading :-
- Operator Overloading allows operators (+, -, *) to work differently for user-defined objects
- Methods :-
1. __add__ (+)
2. __sub__ (-)
3. __mul__ (*)
4. __truediv__ (/)
5. __eq__ (==)
6. __It__ (<)

class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,others):
        return self.marks + others.marks
s1 = student(90)
s2 = student(10)
print(s1 + s2)
=> Data Abstraction :-
- Data Abstraction is prcess of hiding implementation details and showing the essential user data
- Example :- ATM, car, app
- Example :-
from abc import ABC, abstractmethod
class parent:
    @abstractmethod
    def display(self):
        pass

'''

