'''
STRINGS -
=> String is set of characters that are enlposed in '', "", """ """
=> String is immutable

=> Concatination
- Here the (+) operator act as to concatinate moore then 2 strings
- Example :- '''
a = "python"
b = " is a language"
print(a+b)

'''
=> Indexing
- This is used to access the particular char in the string by passing index position value
- We have negative indexing to count positions from first ot last(REVERSE INDEXING)
- Example :- '''
a = "python is a programmimg language"
print(a[12])
print(a[-2])#Reverse indexing 
'''
=> Methods
1.replace():- This method is to change any sub-string to that particular string
- Syntax :- variable_name.replace("old_string","new_string",count)
- Example :-'''
a = "python is a programmimg language"
print(a.replace("python","java",2))
'''
2.join() :- This method used to add a new sub-string after each char in the string
- Syntax :- "string".join(var_name)
- Example :-'''
print("_".join(a))
'''
3.split() :- This method can divide the string into different index into list, based on the string pass by us
- Syntax :-
- Example :- 
4.count():- Used to count the substring in the particular string and also secify the index position
- Syntax :- var_name.count("substring",start_index,end_index)
- Example :- '''
a = "python is a programmimg language"
print(a.count("a"))
'''
=> String Buit-in Functions
1.len() :- This gives the length of the string, which is number chars present in string
- example :-'''
print(len(a))
'''
2.min() :- Will get the min char in string
- Exmaple :- '''
print(min(a))
'''
3.max() :- Will get the max char in string
- Exmaple :- '''
print(max(a))
