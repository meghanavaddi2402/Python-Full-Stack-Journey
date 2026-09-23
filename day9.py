'''
Polymorphism -> Method Overloading, Method Overriding, Operator Overloading
Method Overloading -> Dfault Arguments, variable length arguments, Types of arguments

#Method Overloading (Compile Time Polymorphism) -> Default Arguments
class Hotstar:
    """Default Argument usage"""
    def watch(self,movie = None):
        self.movie = movie
        if self.movie == None:
            print("Welcome to hotstar")
        elif self.movie == movie:
            print(f"User watching {self.movie}")
m = Hotstar()
#m.watch()
m.watch("RRR","Bahubali")

class Hotstar:
    """*args Argument usage"""
    def watch(self,*movie):
        self.movie = movie
##        if self.movie == None:
##            print("Welcome to hotstar")
        for i in movie:
            print(f"User watching {i}")
m = Hotstar()
#m.watch()
m.watch("RRR","Bahubali")

#Method overloading with type of arguments [isinstance()]
#Hotstar => one movie,multiple movie
class Hotstar:
    """Default Argument usage"""
    def watch(self,movie = None):
        print("Welcome to Hotstar")
    def movie_list(self,content):
        self.content = content
        if isinstance(content,str):
            print(f"User Watching {self.content}")
        elif isinstance(content,list):
            print(content)
            for i in content:
                print(i)
m = Hotstar()
m.watch()
#m1 = Hotstar()
#m.movie_list("EEGA")
#m.movie_list(["EEGA","solo","Hello"])
print(m.movie_list(("EEGA","Chalo")))

#Method Overriding -> Inheritance usage
#When the same method name is used in base class and also in derived class super()
class Hotstar:
    def watch(self,movie):
        print("User can watch movies in Hotstar")
class free_user(Hotstar):
    def watch(self,movie):
        super().watch(movie)
        print("with adds")
class Premium_user(free_user):
    def watch(self,movie):
        super().watch(movie)
        print("without adds")
class VIP_user(Premium_user):
    def watch(self,movie):
        super().watch(movie)
        print("without adds and can connect multiple devices")
m = free_user()
m.watch("hello")
'''
#Operator Overloading -> Magic methods/dunder methods) [__init__, __add__]
num1 = 28
num2 = 22
print(num1 + num2)
print(num1.__add__(num2))

print(num1 < num2)
print(num1.__le__(num2))

num = [2, 3, 4, 5, 6]
print(num.__len__())

print("Meghana".__add__("Vaddi"))
print([1, 2, 3].__add__([4, 5, 6]))
