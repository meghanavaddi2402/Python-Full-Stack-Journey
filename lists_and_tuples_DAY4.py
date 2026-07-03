'''
=> LIST DATATYPE :-
- list is a collection of different datatypes that are enclosed in '[]' seperated by ','
- list is mutable
- Methods
1.append() :- this is used to add new item to list, it adds to the last index position in the list
SYNTAX = var_name.append(our_value)
EXAMPLE = 
'''
a = [1,2,3,4]                                  
print(a)                                       
a.append(5)                                    
print(a)
a.append(6)
print(a)
a.append("python")
print(a)
'''
2.extend() :- this works the same as the append() but it assingd the each index for each char given
SYNTAX = var_name.extend(our_values)
EXAMPLE ='''
x = [1,2,3,4]                                  
print(x)
x.append("python")                                    
print(x)
print(len(x))                               
x.extend("python")                                    
print(x)
print(len(x))

'''
3.pop() :- used to delete the item from the list but it will delete based on index position
SYNTAX = var_name.pop(index_value_of_element_to_be_deleted)
EXAMPLE ='''
y = [12, 24, 2, 5, 7]
print(y)
y.pop(0)
print(y)
'''
4.remove():- used to delete the item from the list but it will delete the value from the list but not based on index
SYNTAX = var_name.remove(value_to_be_removed)
EXAMPLE = '''
c = [1, 2, 2, 5, 12]
print(c)
c.remove(12)
print(c)
'''
5.insert()

            mutable                                         immutable
           - the data type can be modified                 - the data type cannoy be modified
           - example :-                                    - example :-
             a = [1,2,3,4]                                  a = "python is a language"
             print(a)                                       print(a.replace("python","java"))
             a.append(5)                                    print(a)
             print(a)
             a.append(6)
             print(a)
=> TUPLE DATATYPE :-
- Tuple is collection of different datatypes that are enclosed in '()' seperated by ','
- Tuple is immutable
- Methods
1.index()
2.count()
EXAMPLE = '''
d = (1,2,3,4,5,"python",[4,5],(9,8,7))
print(d)
print(d[5])
print(len(d))
print(d.index("python"))
print(d.count("python"))
#indexing
b = [1,2,"python is a language",[45,47,"java is a language",[1,23],90],'Hello']
print(len(b))
print(b[3][3][1])
#sorting
l = [1,6,4,7,8,2]
l.sort()
print(l)

l1 = [1,6,4,7,8,2]
l2 = sorted(l1)
print(l2)

