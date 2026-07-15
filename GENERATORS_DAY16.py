'''
=> Generators :-
- This are special functions that returns the iteration, insted of returning all values at once
- Here we are going to use yield keyword
- Example :-
def some():
    yield 1
    yield 2
    yield 3
so = some()
print(next(so))
print(next(so))
print(next(so))


- Working of generator
-> When a function is called it does not execute the function immediately, it returns the generator object, then function will pause at each yield
-> When the next() is called the execution c ontinous from where it is stopped

-> Example:-
def exmp():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")
    yield 3
a = exmp()
print(next(a))
print(next(a))
print(next(a))

-> Example with generator:-
def exmp_1(c):
   for i in range(c):
       yield i*i
a = exmp_1(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

-> Example without generator:-
def exmp_2(c):
   for i in range(c):
       print(i*i)
exmp_2(5)


- yield keyword :-
-> This produces the value
-> But yield pause the function
-> And the yeild will save the current state
-> Yield will continue where it stopped


- next() keyword :-
-> The next() function is used to retrive the next value from generator

-> Example :-
````````````````````def exmp_1(c):
   for i in range(c):
       yield i*i
a = exmp_1(5)
print(next(a))
print(next(a))
print(next(a))


- StopIteration :-
-> Calling next() function after all the values are retrived then it will raise StopIteration error

-> Example :-
def exmp_1(c):
   for i in range(c):
       yield i*i
a = exmp_1(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


- Generator Expression :-
-> The generator expression is similar to list comprehension but uses parantheses () insted of []

-> Example :-
gen =(x*x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
'''
gen =(x*x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
