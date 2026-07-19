'''
class how:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def nam(self):
        print(self.name)
s1 = how("Maggi",34)
print(s1.nam())

=> Methods :- Methods are nothing but the functions inside the class
'''
class calc:
    def add(self, num1, num2):
        print(num1 + num2)
    def sub(self, num1, num2):
        print(num1 - num2)
c = calc()
c.add(2,90)
c.sub(8, 9)
