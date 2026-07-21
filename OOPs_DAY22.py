'''
=>INHERITANCE :- It's a OOP concept where one class(child/derivede) acquires the properties and methods of another class(parent/base) is called inheritance

class parent():
    pass
class child(parent):
    pass

-> Types of Inheritance :-

1. single Inheritance :-
------------------------
- A child clss inherites  from one parent class is single inheritance.
- Example_1 :-

class animals:
    def sound(self):
        print("Animals make sounds")
class dog(animals):
    def bark(self):
        print("Dog barks")
d = dog()
d.sound()
d.bark()

- Example_2 :-

class father:
    def land(self):
        print("5Acr land")
class son(father):
    def flat(self):
        print("3BHK flat")
s = son()
s.land()
s.flat()

2. Multiple Inheritance :-
--------------------------
- A child class inherits from more than one class is called Multiple Inheritance.
- Exmaple :-

class father:
    def skills(self):
        print("Driving...")
class mother:
    def talent(self):
        print("Cooking...")
class brother:
    def waste(self):
        print("Strenght...")
class son(father,mother):
    def mine(self):
        print("Sketching...")
a = son()
a.skills()
a.talent()
a.waste()
a.mine()

3. Multi-Level Inheritance :-
--------------------------
- One child class becomes the parent for other class.
- Example :-

class grandfather:
    def land(self):
        print("Owns a land...")
class father(grandfather):
    def flat(self):
        print("Owns a flat...")
class son(father):
    def car(self):
        print("Owns a car...")
f = son()
f.land()
f.flat()

4. Hierarchical Inheritance :-
--------------------------
- Multiple childs from single parent.
- Example_1 :-

class mother:
    def own(self):
        print("10 kg gold...")
class child1(mother):
    def get1(self):
        print("5kg gold...")
class child2(mother):
    def get2(self):
        print("5kg gold...")
c1 = child1()
c2 = child2()

c1.own()
c1.get1()

c2.own()
c2.get2()

- Example_2 :-

class car:
    def meth_1(self):
        print("It is a automobile")
class tata(car):
    def meth_2(self):
        print("TATA is a car model")
class kia(car):
    def meth_3(self):
        print("KIA is a car model")
c1 = tata()
c2 = kia()

c1.meth_1()
c1.meth_2()

c2.meth_1()
c2.meth_3()

5. Hybrid Inheritance :-
--------------------------
- This is combination of two or more types of inheritance.
- Example :-  Multiple Inheritance +  Multi-Level Inheritance

class a:
    def m1(self):
        print("CLASS A")
class b(a):
    def m2(self):
        print("CLASS B")
class c(a):
    def m3(self):
        print("CLASS C")
class d(b,c):
    def m4(self):
        print("CLASS D")
cl = d()
cl.m1()
cl.m2()
cl.m3()
cl.m4()

=> super() :-
- This function is used to parent class methods or constructor in the child class.
- Example :-

class father:
    def show(self):
        print("Parent Class...")
class child(father):
    def show(self):
        super().show()
        print("Child Class...")
c = child()
c.show()

class person:
    def __init__(self, name):
        self.name = name
class student(person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        print(self.name)
        print(self.roll)
an = student("Maggi", 429)
an.display()
'''
