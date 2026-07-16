'''
=> MODULES :-
- A module is a python file(.py) that contains reusable code
1. Functions
2. Variables
3. Classes
4. Objects
5. Statements
- Why this..??
    Insted of writing the same code, we can store in a module and use whenever needed
- Types of modules :-
1. User-Defined :-
-> Example importing a module :-
import my_file
print(my_file.add(10,8))
print(my_file.div(10,8))
print(my_file.mul(10,8))
print(my_file.sub(10,8))
print(my_file.power(10,8))
print(my_file.floor_division(10,8))

-> Example importing a specific function in a module :-
from my_file import add
print(add(10,8))


-> Example importing a module as alias :-
import my_file as m
print(m.sub(9,6))

2. Built-In :-
-> math :-
    EXAMPLE :-
import math
print(math.sqrt(25))
print(math.factorial(25))
print(math.pow(25))
print(math.pi)

sqrt      --->     square root
factorial --->     factorial
pow       --->     power 
pi        --->     pi value
ceil      --->     round up

-> os :- The os module is used to interact with operating system
    EXAMPLE :-
import os
print(os.getcwd())
#os.mkdir("me")
os.rmdir('me')

getcwd   --->    Current Directory
mkdir    --->    Creates Directory
rmdir    --->    Remove Directory

-> sys :- This will provide informatio about python intepreter
    EXAMPLE :-
import sys
print(sys.version)

-> random :- Used to generate random values
    EXAMPLE :-
import random
print(random.randint(1000,9999))
'''

import random
print(random.randint(1000,9999))

colour = ['Red', 'Green', 'Blue', 'White', 'Orange', 'Black']
print(random.choice(colour))
