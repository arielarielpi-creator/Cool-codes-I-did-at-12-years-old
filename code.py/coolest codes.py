#exe 1
secret = input("Write a 4-digit code\n")
while len(secret) != 4:
   secret = input("Your code is not 4 digits long, please write a valid one\n")
if len(secret) == 4:
    secret = int(secret)
    for code in range(0, 10000):
        print(code)
        if code == secret:
            print(f"I successfuly cracked your code, the code was : {code}")
            break


#exe 2
import random

words = ["milk", "python", "school", "computer", "banana", "orange", "keyboard", "monitor"]

word = random.choice(words)
display = "_" * len(word)
attempts = 15

print("Welcome to the game!")
print(display)
print("You have", attempts, "attempts.")

while "_" in display and attempts > 0:
    guess = input("Guess a letter: ")
    guess = guess[0]

    new_display = ""

    for i in range(len(word)):
        if word[i] == guess:
            new_display += guess
        else:
            new_display += display[i]

    if new_display == display:
        print("The letter is not in the word.")
    else:
        print("Good guess!")

    display = new_display
    attempts -= 1

    print(display)
    print("Attempts left:", attempts)

if display == word:
    print("You won!")
else:
    print("You lost! The word was:", word)


#exe 3
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


#exe 4
score = 0
print("you have to guess the tricky password and every time you will try to guess it, it will change. there are 4 steps and every time you succeed your score will go up. (it's much easier than it looks)")
print("")
a = input("enter password: ")
b = "password"
if a == b :
    score += 25
else:
     score +=0
c = input("try again ")
d = "again"
if c == d :
     score += 25 
else:
     score += 0
e = input("the password is incorrect ")
f = "incorrect"
if e == f :
     score += 25
else:
     score +=0
g = input("please try to remember ")
h = "to remember"
if g == h :
     score += 25
else:
     score +=0
print(f"your score is {score}")


#exe 5
while True:
    ASCII = int(input("1 = do you want to enter a letter to see the ASCII number of the letter. 2 = or do you want to enter a number to see what is the letter that this is her ASCII number. chose 1 or 2\n"))
    if ASCII == 1: 
        word = input("ok so enter a letter to see the ASCII number of the letter\n")
        print(ord(word))
    else:
        number = int(input("ok so enter a number to see what is the letter that this is her ASCII number\n"))
        print(chr(number))


#exe 6
password = input("enter your password\n")
if password[0].isupper():
    if "&" in password or "#" in password or"!" in password:
      print("ok your password is valid")
    else:
      input("you need & or # or ! in your password, enter your password again\n")
elif "&" in password or "#" in password or"!" in password:
    input("your password must start with a capital letter, enter your password again\n")
else:
    input("your password must start with a capital letter and need to contain & or # or !, enter your password again\n")


#exe 7
import random
import time
# colors
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BLACK       = "\033[30m"
RED         = "\033[31m"
GREEN       = "\033[32m"
YELLOW      = "\033[33m"
BLUE        = "\033[34m"
MAGENTA     = "\033[35m"
CYAN        = "\033[36m"
WHITE       = "\033[37m"

BRIGHT_BLACK   = "\033[90m"
BRIGHT_RED     = "\033[91m"
BRIGHT_GREEN   = "\033[92m"
BRIGHT_YELLOW  = "\033[93m"
BRIGHT_BLUE    = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN    = "\033[96m"
BRIGHT_WHITE   = "\033[97m"
# backround
BG_BLACK    = "\033[40m"
BG_RED      = "\033[41m"
BG_GREEN    = "\033[42m"
BG_YELLOW   = "\033[43m"
BG_BLUE     = "\033[44m"
BG_MAGENTA  = "\033[45m"
BG_CYAN     = "\033[46m"
BG_WHITE    = "\033[47m"

BG_BRIGHT_BLACK   = "\033[100m"
BG_BRIGHT_RED     = "\033[101m"
BG_BRIGHT_GREEN   = "\033[102m"
BG_BRIGHT_YELLOW  = "\033[103m"
BG_BRIGHT_BLUE    = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN    = "\033[106m"
BG_BRIGHT_WHITE   = "\033[107m"
# סגנונות נוספים
BOLD       = "\033[1m"
ITALIC     = "\033[3m"
UNDERLINE  = "\033[4m"
INVERSE    = "\033[7m"
# סיום 
RESET = "\033[0m"

mydict = {
    "names": ["daniel", "ariel", "ilay"],
    "numbers": {
        "small": [11, 82, 35, 67],
        "big": [555, 666, 777, 888]
    },
    "cars": ["Lambo", "Mercedes", "Toyota"]
}

for key, value in mydict.items():
    time.sleep(0.5)
    if key == "names":
        print(BRIGHT_GREEN + f"{key} : {value}" + RESET)
    elif key == "numbers":
        print(BRIGHT_YELLOW + f"{key} : {value}" + RESET)
    elif key == "cars":
        print(BRIGHT_CYAN + f"{key} : {value}" + RESET)

time.sleep(0.5)
print(BLUE + BOLD + BG_BLACK + "|==>                  <==|" + RESET)
print(RED + BOLD + BG_BLACK + ITALIC + "|==> now the new dict <==|" + RESET)
print(GREEN + BOLD + BG_BLACK +"|==>                  <==|" + RESET)
time.sleep(0.5)


mydict["names"] = [name[0].upper() + name[1:-1] + name[-1].upper() for name in mydict["names"]]
mydict["numbers"]["small"] = [bigger * random.randint(5, 10) for bigger in mydict["numbers"]["small"]]
mydict["numbers"]["big"] = [smaller // random.randint(2, 5) for smaller in mydict["numbers"]["big"]]
mydict["cars"] = ["Lamburgini", "Ferrari", "Tesla"]
random.shuffle(mydict["cars"])


for key, value in mydict.items():
    time.sleep(0.5)
    if key == "names":
        print(BRIGHT_CYAN + f"{key} : {value}" + RESET)
    elif key == "numbers":
        print(BRIGHT_YELLOW + f"{key} : {value}" + RESET)
    elif key == "cars":
        print(BRIGHT_GREEN + f"{key} : {value}" + RESET)


#exe 7
