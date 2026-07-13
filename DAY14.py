'''
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

=>filter() :-
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

=> LIST COMPHERENSION :-
- This offers a shorter syntax whwn we want to create a new list from the old one
- Syntax :- variable_name = [expression loop condition]
- Example :-
a = [1,2,3,4,5,6]
b = [j for j in a]
print(b)


- Example :-
a = [1,2,3,4,5,6]
b = [j for j in a if j % 2 == 0]
print(b)

=> DICTIONARY COMPHERENSION :-
- This offers a shorter syntax when we want to create a new dictionary from old dictionary
- Syntax : - variable_bame - [expression loop]
- Example :-
old_dict = {1:2, 3:7, 8:0}
new_dict = {i:j for(i,j) in old_dict.items() if j % 2 == 0}
print(new_dict)
'''

txt = ("Python iS A ProGraMMing LnaGuAge ")
cap_count = 0
space_count = 0
small_count = 0
def cap_small(txt,cap_count, space_count , small_count):
    for j in txt:
        if j.isupper():
            cap_count  += 1
        elif j.islower():
            small_count += 1
        else:
            space_count += 1
    print(f"The total number of capital letters are {cap_count}")
    print(f"The total number of small letters are {small_count}")
    print(f"The total number of spaces letters are {space_count}")
cap_small(txt,cap_count, space_count , small_count)
    
    

    
