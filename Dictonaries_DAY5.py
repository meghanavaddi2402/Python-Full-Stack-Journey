'''
=> DICTIONARY DATA TYPE
- Dictionary is a key : value pair seperated by :, and keys are unique
- In the place of keys we have use immutable data type
'''
a = {"name" : "meghana", "number" : [[1,2],[3,4]]}
print(a)
'''
- Methods :-
1.keys() :- used to get all the keys from the dictionary
SYNTAX :- variable_name.keys()'''
details = {"name" : "meghana",
           "age" : 7,
           "gender" : "F"}
print(details.keys())
'''
2.values() :- used to get all the values from the dictionary
SYNTAX :- variable_name.values()'''
details = {"name" : "meghana",
           "age" : 7,
           "gender" : "F"}
print(details.values())
'''
3.items() :- used to get all the items(key and value pair) from the dictionary
SYNTAX :- variable_name.items()'''
details = {"name" : "meghana",
           "age" : 7,
           "gender" : "F"}
print(details.items())

d1 = {"name" : "x",
      "age" : 19,
      "phone_number" : 1234567890,
      "id_number" : 429,
      "section" : "EEE-5"}
print(d1["phone_number"])
'''
4.clear() :- clears every item in the dictionary
SYNTAX :- variable_name.clear()'''
d1 = {"name" : "x",
      "age" : 19,
      "phone_number" : 1234567890,
      "id_number" : 429,
      "section" : "EEE-5"}
d1.clear()
print(d1)
'''
5.update() :- update the value of key in the dictionary
SYNTAX :- variable_name.update({"key_name" : "new_value"})'''
details = {"name" : "meghana",
           "age" : 7,
           "gender" : "F"}
d1.update({"name" : "charan",
           "age" : 19,
           "gender" : "M"})
d1.update({"mobile_number" : "0987654321"})

print(d1)


'''
=> SET DATA TYPE
- Set is collection of unordered elements seperated by ","
- Sets are mutable
- can remove duplicates by itself 
'''
s = {1,2,3,4,5,1}
print(s)
'''
- Methods
1.union()[|] :- combines the elements from both sets
SYNTAX :- set_1.update(set_2)
'''
s = {1,2,3,4,5}
s1 = {5,6,7,8,9}
print(s | s1)
print(s.union(s1))
'''
2.intersection()[&] :- common elements from both sets
SYNTAX :- set_1.intersection(set_2)
'''
s = {1,2,3,4,5}
s1 = {5,6,7,8,9}
print(s & s1)
print(s.intersection(s1))
'''
3,symmetric difference()[^] :- different elements from both sets
SYNTAX :- set_1.symmetric_difference(set_2)
'''
s = {1,2,3,4,5}
s1 = {5,6,7,8,9}
print(s ^ s1)
print(s.symmetric_difference(s1))
'''
4.add() :- used to add new element
SYNTAX :- set.add(value)
'''
s = {1,2,3,4,5}
s.add(10)
print(s)

'''
5.remove() :- to delete elements from set
SYNTAX :- set.remove(value)
'''
s = {1,2,3,4,5}
s.remove(3)
print(s)

'''
6.discard() :- to delete elements from set and does not throw error although the element is not there in the set
SYNTAX :- set.discard(value)
'''
s = {1,2,3,4,5}
s.discard(10)
print(s)
s.remove(10)
print(s)
