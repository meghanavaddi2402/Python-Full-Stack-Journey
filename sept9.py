'''
POP(procedure oriented programming) - Dividing the entire code into blocks(procedures)
Procedures are created using functions(def)
Function :- A reusable block of code (A block of statements which perform a specific task)
Syntax:-
def <Function_Name>(parameters): #Function Definition
    """Doc String"""
    .....Statement(s)..
    ...................
    ................... #Body of Function
    return value(s)...
Function_Name(args) #Function Call

#Simple Example
def add(a,b):
    """Addition Function"""
    return a+b
print(add(11234,90988)) #addition
c,d = 'codegnan','python'
print(add(c,d)) #concentation
e,f = map(str,input("Enter values: ").split(','))
print(add(e,f))
print(add([1,2,3,4],[5,6,7,8]))#merging
#print(add(1,2,3,4))#positional arguments
# variable length arguments => *args (we can pass any number of positional arguments)
#arguments - Data is stored in tuples

def sample(*a):
    """Demo of variable length arguments"""
    print(a)
    print(type(a))
sample()
sample(1,234,44,56,8,7,43,65,56)
sample("maggi",24,2,["hello","hi","thank","you"],{23,32,2,76,43})
marks = [23,32,2,76,43]
sample(marks)
sample(*marks)
a,*b,c = 23,"hello",34,543,33,24,43,23
print(a)
print(b)
print(c)

def add(*a):
    """Perform addition for numeric values"""
    print(a)
    result = 0
    for i in a:
        #print(i)
        if type(i) in [int,float]:
            result += i
    return result
print(add(1,2,3))
print(add(1,"hello",8,9))

#keyword arguments - We can pass the name of argument
def batch(name,age,place="Vizag"):
#def batch(name="x",age,place="Vizag"): => It rises error non-default always follows a default argument 
    """KEyword arguments usage"""
    print(f"{name} is in {place} and of {age} years old.")
batch("Meghana",21,"vizag")
batch(place="Vizag",name="Meena",age=22)#Keyword arguemt no need order but needs name
batch(name="Cherry",age=19)#Default arguments can accept a value as default
batch(name="x",age=21,place="hyd")


print(4,5) #output = 4 5 as seperated by space by default
print(4,5,sep=',')# here keyword argument is sep and we are changing default value for sep output = 4,5
'''
#keyword variable lenght arguments (**kwargs) - Any number of arguments
#In keyword arguments, data is stroed in dictionaries
def batch(**a):
    """Keyword varibl length argument usage"""
    print(a)
    print(type(a))
batch()
batch(name="Cherry",age=19,branch="CSE")
data = {'names':['Arjun','Vikram'],
        'places':['Vizag','Hyderbad']}
#batch(**data)
data.update({'batch':'PFS-VSP-007'})
batch(**data)


#Create a function using *args and **kwargs

