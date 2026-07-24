'''
=> Error Handling :-

-> Syntax Error :-
- EXAMPLE :-
for j in range(1,10:
    print(j)
OUTPUT - SyntaxError

-> IndendationError :-

- EXAMPLE :-
    a=20
for i in range(a):
    print(a)
else:
    print()

->ValueError :-
- EXAMPLE :-
x = int(input("Enter a number: "))
OUTPUT - ValueError

-> Error Handling:-
- try :- Try block will test the code for error.
- SYNTAX :- try:
                ---------------
                ---------------
                ---------------
                ----try code---

                
- except :- Except handles error in the code.
- SYNTAX :- except:
                ---------------
                ---------------
                ---------------
                --except code--
- EXAMPLE :-
try:
    print(num)
except:
    print("NameError")
    
- By using NameError it handles only name error, but not any other errors
try:
    print(num)
except NameError:
    print("NameError") #This gives NameError

    
try:
    n = int(input("Enter a integer: "))
except NameError:
    print("NameError")  #This doesn't get NameError but gives ValueError

- EXAMPLE :-
try:
    n1 = int(input("Enter n1 value: "))
    n2 = int(input("Enter n2 value: "))
    print(n1/n2)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")


    
- else :- If the try block doesn't have error then the else block is excuted
- SYNTAX :- else:
                ---------------
                ---------------
                ---------------
                ---else code---
- EXAMPLE :-
try:
    n1 = int(input("Enter n1 value: "))
    n2 = int(input("Enter n2 value: "))
    print(n1/n2)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
else:
    print("NoError")

- finally :- The finally block will execute either code has errors or no errors
- SYNTAX :- finally:
                ----------------
                ----------------
                ----------------
                --finally code--
- EXAMPLE :-
try:
    n1 = int(input("Enter n1 value: "))
    n2 = int(input("Enter n2 value: "))
    print(n1/n2)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
else:
    print("NoError")
finally:
    print("----End----")
'''
