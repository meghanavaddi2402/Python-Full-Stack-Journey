'''
=> LOOPS
1.for loop
- A foor loop is used to iterate over a sequence, list, tuple, dictionaries
- Example_1 :- for string
    for i in a:
    print(i) #'i' is a instance variable
    
- Example_2 :- for list
    b = [1,2,3,4,5]
    for j in b:
        print(j)
        
- Example_3 :- for tuple
    b = {9,6,9,3,5,0,1}
    for j in b:
        print(j)
        
- Example_4 :- for dictinoary
    c = {"name" : "x",
     "age" : 23,
     "student id" : 12345}
    for h in c.keys():
        print(h)
    for h in c.values():
        print(h)
    for h in c.items():
        print(h)
- else in for loop
   The else block will be executed after the for loop, but incase the loop is breaked then it will never enter into else block
    Example_1 :-
    b = [1,2,3,4,5]
    for j in b:
        print(j)
    else:
    ("done")  #output:- 1 2 3 4 5  done
    Example_2 :-
    b = [1,2,3,4,5]
    for j in b:
        print(j)
        if j == 3:
            break
    else:
        ("done")

2.while loop
- The while loop will execute until the condition becomes true
- Example :-
    i = 1
    while i < 5:
        print(i)
        i += 1
=> CONTROL STATEMENTS
1.break - The break staatement is used to exit from the loop
- Example :-
    b = [1,2,3,4,5]
    for j in b:
        print(j)
        if j == 3:
            break
    else:
        ("done")
2.continue :- This will skip the current iteration if contions matches
- Example :-
    b = [1,2,3,4,5]
    for j in b:
        if j == 3:
            continue
        print(j)
    else:
        ("done")
3.pass :- Space holder
range() :- range is a buit-in function it is used to generate sequence upto limit 
- Syntax :- range(start_value, end_value, step)
- Example :-
    b = [1,2,3,4,5]
    for j in range(1,51):
        print(j)
*** assert keyword :- it is useed to check condition, but it will rise error incase it is false
- Example :-
    i = int(input("Enter age: "))
    assert i >= 18, "you must be 18 years old"
    print(f"your {i} years old ")
    
'''

