'''
PASS BY VALUE
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




'''

