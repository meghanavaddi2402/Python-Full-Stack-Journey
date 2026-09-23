
'''
random model -> helps to generate random values
OTP generation,Story,Games(Rock Paper Scissors)

import random, time
#random number generator
a = random.randint(1000,9999)
#print(a)

for i in range(5):
    time.sleep(3)
    print(random.randint(1000,9999))
    #time.sleep(3)->sleep(seconds) - helps for waiting for a period

#Rock Paper Sissors
import random, time
for i in range(10):
    player1 = input("Enter one of this -> Rock,Paper,Sissors ").lower().strip()
    player2 = random.choice(["Rock", "Paper" ,"Sissors"]).lower()
    #print(player1)
    print(player2)
    count1 = 0
    count2 = 0
    if player1 == "rock" and player2 == "paper":
        print("player2 won!!!")
        count2 += 1
    elif player1 == "paper" and player2 == "scissors":
        print("player2 won!!!")
        count2 += 1
    elif player1 == player2:
        print("Tie")
    else:
        print("player1 won!!!")
        count1 += 1
total = count1 + count2
print("---------- Final Result ----------")
print(f"Player 1 wins: {count1}")
print(f"Player 2 wins: {count2}")
print(f"Total games with a winner: {total}")

when = ['A long back', 'Once upon a time', 'Few Years ago']
who = ['Devara', 'King in the France', 'Barbie Queen']
what = ['A Magical Sword', 'Powerful Hammer', 'Unlimited Arrows']
where = ['Far in the Galaxy', 'End of Ocean', 'in india']
how = ['War Started', 'Both fought for 15days', 'Sad Ending']
#To create a story - link when to what to who to how...
print(random.choice(when) + " " + random.choice(who))

#Bussiness card generator - name,email_id,ph number, website link using segno
import segno
print(dir(segno))
from segno import helpers
qr = helpers.make_mecard(name = "meghana", email="meghanavaddu2402@gmail.com", phone="+91 9533759479", birthday="2005-02-24",url="https://www.linkedin.com/in/meghana-vaddi-5902722a7/")
print(qr)
qr.save("mydetails.png",scale = 10)

#Rock Paper Sissors
import random, time
count1 = 0
count2 = 0
played = 0
ties = 0
choices = ["rock", "paper" ,"scissors"]

rounds = int(input("Enter number of round: "))
while played<rounds:
    you = input(f"Enter one of this {choices}: ").lower().strip()
    if you not in choices:
        print("VERIFY YOUR CHOICES!!!\n")
        break
    played += 1
    computer = random.choice(choices).lower()
    print(f"computer choice: {computer}")

    if you == computer:
        print("Tie")
        ties += 1

    elif you == "scissors" and computer == "rock":
        print("Computer won!!!")
        count2 += 1

    elif you == "rock" and computer == "paper":
        print("Computer won!!!")
        count2 += 1
    elif you == "paper" and computer == "scissors":
        print("Computer won!!!")
        count2 += 1
    else:
        print("You won!!!")
    print(f"Your score: {count1}")
    print(f"Computer score: {count2}")
    print("-" * 50)
print("========== Final Result ==========")
print(f"Your wins: {count1}")
print(f"Computer wins: {count2}")
print(f"Total ties : {ties}")
print(f"Total games: {played}")

'''

import random

def number_game():
    print("\n===== Number Game =====")
    number = random.randint(1, 10)
    for i in range(3):
        guess = int(input(f"Guess {i + 1} - Enter a number between 1 and 10: "))
        if guess == number:
            print("Correct! You won!")
            break
        elif guess < number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
    else:
        print(f"Sorry! You used all 3 guesses.")                    


def rock_paper_scissors():
    print("\n===== Rock Paper Scissors =====")
    choices = ["rock", "paper", "scissors"]
    user = input("Enter rock, paper or scissors: ").lower()
    computer = random.choice(choices)

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif(user == "rock" and computer == "scissors") or(user == "paper" and computer == "rock") or(user == "scissors" and computer == "paper"):
        print("You won!")
    else:
        print("Computer won!")


def study_option():
    print("\n===== Study Option =====")
    print("1. Python")
    print("2. SQL")
    print("3. JavaScript")
    print("4. React")
    choice = input("Choose a subject: ")
    if choice == "1":
        print("Study Python: Variables, Data Types, Functions, OOP")
    elif choice == "2":
        print("Study SQL: SELECT, WHERE, JOIN, GROUP BY")
    elif choice == "3":
        print("Study JavaScript: Functions, Arrays, DOM")
    elif choice == "4":
        print("Study React: Components, Props, State, Hooks")
    else:
        print("Invalid choice")


while True:
    print("\n========== CHOICE GAME ==========")
    print("1. Number Game")
    print("2. Rock Paper Scissors")
    print("3. Study Option")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number_game()

    elif choice == "2":
        rock_paper_scissors()

    elif choice == "3":
        study_option()

    elif choice == "4":
        print("Thank you! Bye!")
        break

    else:
        print("Invalid choice. Please select 1-4.")

    
