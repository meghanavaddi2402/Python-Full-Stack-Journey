'''
=> INPUT FORMATTING FROM USER
-> input() :- function is used to take input from user
1.int()
- Example :-
num = int(input("Enter a number: "))
num1 = int(input("Enter a number: "))
print(num + num1)

2.string()
- Example :-
num = (input("Enter a string: "))
num1 = (input("Enter a string: "))
print(num + num1)

3.float()
- Example :-
num = float(input("Enter a number: "))
num1 = float(input("Enter a number: "))
print(num + num1)

4.list()
- Example :-
grp = list(map(int,input().split()))
print(grp)

5.tuple()
- Example :-
tup = tuple(map(int,input().split()))
print(tup)


tup = tuple((input().split()))
print(tup)


n = eval(input())
print(type(n))
'''




name = input()
age = int(input())
print(name,"you're age",age)
print(f"{name} you're age is {age}")
print("your name is %s and your %d old" %(name, age))
