'''
=> STATEMENTS
1.Condition Statements
- if -> checks if condition is true or not
  EXAMPLE :-
    num = 8
    if num % 2 == 0:
        print(f"{num} even")
- if else ->
  EXAMPLE :-
    num = 8
    if num % 2 == 0:
        print(f"{num} even")
    else :
        print(f"{num} odd")
- nested if -> if isnside if is called as nested if
  EXAMPLE :-
    details = {"atm pin" : '2402'}
    pin = input("Enter pin: ")
    if len(pin) == 4:
        if pin in details['atm pin']:
            print("welcome to atm")
        else:
            print("incorrect pin")
    else :
        print("enter 4 digit pin")

- elif ->
  EXAMPLE :-
    m = int(input())
    if m >= 90:
        print("A+")
    elif m >= 80:
        print("A")
    elif m >= 70:
        print("B+")
    elif m >= 60:
        print("B")
    elif m >= 50:
        print("C+")
    elif m >= 40:
        print("C")
    else:
        print("FAILED")

2.Control Statements
3.Loops
'''





lst = list(map(int, input("Enter numbers separated by space: ").split()))
if len(lst) == 3:
    print(max(lst))
else:
    print("enter only 3 numbers")


ch = input("Enter alphabet: ")
if((ch == 'A')or (ch == 'a') or (ch == 'E') or (ch == 'e') or (ch == 'I') or (ch == 'i') or (ch == 'O')or (ch == 'o') or (ch == 'U') or (ch == 'u')):
    print(f"{ch} is a vowel")
else:
    print(f"{ch} is a consonent")
