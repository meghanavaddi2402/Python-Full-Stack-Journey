'''
=> FUNCTIONS
- Function is a block of code that cn be reused
- Functions can avoid the repeted lines of code
- Functions are of 2 types
1.Buit-in functions
- Examples :- print(), max(), type(), min() etc...
2.User defined functions
- This function starts with the keyword 'def'
- Syntax :-
    def function_name(parameters):
        --------------------
        --------------------
        -------------------
    function_name(arguments) #calling function
- Example :-
def add(a, b):
    print(a+b)
add(9,2)

- Types of arguments :-

-> Required arguments :-
    we have to pass the same number of arguments as in definition of function
   EXAMPLE1 :-
def add(a, b):
    print(a+b)
add(9,2)         #This gives output 9 + 2 = 12
   EXAMPLE2 :-
def add(a, b):
    print(a+b)
add(9,2,1)        #This gives output as TypeError: add() takes 2 positional arguments but 3 were given

-> Default :-
    EXAMPLE :-
n = 2
n1 = 3
n2 = 8
def add(a, b, c):
    print(a)
    print(b)
    print(c)
add(n,n1,n2)

-> Keyword :-
    we can pass as a using variable names like (variable_name = data_type)
   EXAMPLE :-
def add(a, b):
    print(a+b)
add(a=9,b=2)

-> Variable length :-
    Can pass n number of arguments and by just using (*args) in parameters, will recive tuple of arguments
   EXAMPLE1 :-
n = 2
n1 = 3
n2 = 8
def add(a, b, c):
    print(a)
    print(b)
    print(c)
add(n,n1,n2)

    EXAMPLE2 :- for lists (**args)
def funt(**any):
    print(any['name'])
funt(name = "x", age = 24)

GLOBAL VARIABLE :- This variable can be used throught the programm
EXAMPLE :-

num = 9   #This global variable
def any():
    print(num)
any()
print(num)


def any():
    num = 9   #Thisis local variable it cannot be accessed outside function
    print(num)
any()
print(num)

num = 9   #This global variable
def any():
    global num
    num = 24
    print(num)
any()
print(num)

def some(a):
    for j in a:
        print(j)
some([12,34,5,6,564,54,565])
=> Return Keyword :- I n a function if a return executed then it will exit from function with certain returned values
- EXAMPLE
def some(b):
    return 5 + b
a = some(10)
c = some(9)
print(a)
print(c)


import builtins
builtin_functions = [name for name in dir(builtins) if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"total buit-in functions are {len(builtin_functions)}")

=> Recursive Functions
- Recursive function that calls itself repeatedly until specific condition is met
- Synatax :-
def funtion_name(parameters):
    if condition -> base case
        return statement
    else :
        return statement
- EXAMPLE :-
def my_funt(num):
    if num == 1:
        return 1
    else :
        return num * my_funt(num - 1)
num = 10
print(my_funt(num))

=> LAMBDA FUNCTION :-
- It is also called as annonymous function
- A lamba function can take n number of arguments but having only one expression
- Syntax :- lambda aguments : expressions
- Example :-
funt_1 = lambda a : a+5
print(funt_1(25))
- Example :-
funt_2 = lambda a,b,c : a+b+c
print(funt_2(25,5,0))

=>filter()
- The filter is a buit-in function used to filter elements from an iterables such as list, tuples and sets based on condition
- Syntax :- filter(function, iterable)
- This filter() function returns object so we can convert that into lits, set and tuple
- Example :-
num = [1,2,3,4,5,6,7]
rev = filter(lambda a : a%2 == 0,num)
print(list(rev))

- Example :-
num_1 = [1,2,3,4,5,6,7]
a = filter(lambda a : a%2 != 0,num_1)
print(set(a))

'''


num = [1,2,3,4,5,6,7]
rev = filter(lambda a : a%2 == 0,num)
print(list(rev))


num_1 = [1,2,3,4,5,6,7]
a = filter(lambda a : a%2 != 0,num_1)
print(a)
