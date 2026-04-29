#exe 1
name = input("What is your name?\n")
print(f"Okay, nice to meet you {name}!")
print("\nWelcome to our website! You need to create a password so all your progress won't be lost when you enter our website again")
print("Your password must start with a capital letter and need to contain one of these symbols: #, !, &.\n")
while True:
    password = input("Enter your password:\n")
    if not password:
        print("You must enter a password!")
        continue
    if not password[0].isupper() and not any(symbol in password for symbol in ["#", "!", "&"]):
        print("your password must start with a capital letter and need to contain one of the following symbols: #, &, !.")
        continue
    if not password[0].isupper():
        print("Your password must start with a capital letter.")
        continue
    if not any(symbol in password for symbol in ["#", "!", "&"]):
        print("Your password must contain one of the following symbols: #, !, &.")
        continue
    print("ok! Your password is valid ")
    break


#exe 2
import random
print("You are going to play a game where you have to guess the number chosen, the number is between one and 100.\n")
a = random.randint(1,100)
attempts = 1
b = int(input("guess a number betwen 1 and 100\n"))
while b != a:
    if b < a:
        print("You need to choose a bigger number.")
    elif b > a:
        print("You need to choose a smaller number.")
    b = int(input("Choose again: "))
    attempts += 1
print(f"You guessed it correctly! 🎉, the number is {a}, it took you {attempts} attempts")


#exe 3
sentence = input("write a sentence\n")
letter = input("write a letter to count\n")
count = 0
for times in sentence:
    if times == letter:
        count += 1
print(f"the letter {letter} appears {count} times in the sentence")


#exe 4
count = int(input("How many numbers do you want to enter? "))
total = 0
for i in range(count):
    number = float(input(f"Enter number #{i+1}: "))
    total += number
average = total / count
print(f"The average of the numbers is {average}")


#exe 5
while True:
    a = int(input("what is your age?\n"))
    if a>120 or a<=0:
        print("you are lying about your age")
    if a<12 and a>0:
        print("you can't come to my party")
        break
    if a>12 and a<18:
        print("you can stay in my party until 11 pm")
        break
    if a>20 and a<40:
        print("you can stay in my party how much you want")
        break
    if a>40 and a<120:
        print("you are too old to be in my party")
        break


#exe 6