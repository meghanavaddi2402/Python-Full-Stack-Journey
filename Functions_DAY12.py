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
'''
