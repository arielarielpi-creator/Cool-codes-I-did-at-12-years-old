#exe 1
import time
for num in range(1, 11):
    print(num)
    time.sleep(0.3)


#exe 2
total = 0
numbers = [2,64,71,8,67]
for number in numbers:
    total += number
    print(f"number is: {number}")
    print(f"total is: {total}")


#exe 3
import time
name = "ariel"
for letters in name:
    print(letters)
    time.sleep(0.3)


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
word = input("what is your name\n")
if word[0].isupper():
    print("you wrote your name correct, it begins with a capital letter") 
else:
    print("you didnt wrote your name correct, it doesnt begins with a capital")


#exe 7
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


#exe 8
new_names = []
names = ["ariel", "daniel", "ilay", "eitan", "maor"]
for name in names:
    new = name.replace(name[0], name[0].upper())
    new_names.append(new)
print(new_names)


#exe 9
x = int(input("Choose a number to see if it is even or odd\n"))
if x % 2 == 1:
    print("odd")
elif x % 2 == 0:
    print("even")


#exe 10
a = int(input("enter a number\n"))
b = int(input("enter another number\n"))
c = int(input("enter one last number to see what is the average of the numbers\n"))
d = a+b+c
print(f"the average is: {d/3}")


#exe 11
import random
print("You and the computer are going to compete in a game where you have to guess a number between one and 100 and whoever is closest to the randomly chosen number wins.\n")
target_number = random.randint(1,100)
user_number = int(input("enter your number\n"))
computer_number = random.randint(1,100)
if target_number >= user_number:
    user_diff = target_number - user_number
else:
    user_diff = user_number - target_number

if target_number >= computer_number:
    computer_diff = target_number - computer_number
else:
    computer_diff = computer_number - target_number
if user_diff < computer_diff:
    print(f"you won, the target number was {target_number}, the computer number was {computer_number} and your number was {user_number}")
elif user_diff > computer_diff:
    print(f"the computer won, the target number was {target_number}, the computer number was {computer_number} and your number was {user_number}")
else:
    print(f"it is a tie, the target number was {target_number}, and your numbers were {user_number}")


#exe 12
user_input = input("Write an equation:\n")
a = int(user_input[0])
b = int(user_input[3])
c = int(user_input[5])
x = (c-b)/a
if ".0" in str(x):
    print("x:", int(x))
else:
    print(x)


#exe 13
password = input("enter a password\n")
while True:
    if len(password) < 6:
        password = input("the password should be at least 6 characters long, please enter a new one\n")
        continue
    if not any(i.isdigit() for i in password):
        password = input("password must include at least one number, please try again\n")
        continue
    if not any(i.isalpha() for i in password):
        password = input("password must include at least one letter, please try again\n")
        continue
    break
print(f"your password is {password}, it is valid")


#exe 14
text = input("please enter a text\n")
count_numbers = 0
count_letters = 0
count_spaces = 0
length = len(text)
for i in text:
    if i.isdigit():
        count_numbers += 1
    if i.isalpha():
        count_letters += 1
    if i == " ":
        count_spaces += 1
print(f"your text has {count_numbers} numbers, {count_letters} letters and {count_spaces} spaces")


#exe 15
import time
attempts = 3

while True:
    password = input('Enter password: ')
    time.sleep(1)
    for i in password:
        if password.count(i) >2:
            print("you can't put the same sign in your password more than twice\n")
            break
    if len(password) > 12 and password.count(i) >2:
        print("access granted")
        break
    else:
        attempts -= 1
        print(f"your passord should be longer than 12 characters, Attempts left: {attempts}")
    if attempts == 0:
        print("system locked")
        break


#exe 16
a = "ar+iel3 3pin+kas"
count_numbers = 0
count_letters = 0
count_spaces = 0
count_pluses = a.count("+")
for i in a:
    if i.isdigit():
        count_numbers += 1
for i in a:
    if i.isalpha():
        count_letters += 1
for i in a:
    if i.isspace():
        count_spaces += 1
print(count_numbers)
print(count_letters)
print(count_spaces)
print(count_pluses)


#exe 17
word = input("please enter a word to see if its a palindrom ot not\n")
check = word[::-1]
if word == check:
    print("palindrom")
else:
    print("not palindrom")


#exe 18
import time
while True:
    print("What do you want to do?")
    time.sleep(2)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choise = input("choose 1, 2, 3, 4, 5\n")
    if choise == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"Result: {num1:g} + {num2:g} = {result:g}")
    elif choise == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print(f"Result: {num1:g} - {num2:g} = {result:g}")
    elif choise == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print(f"Result: {num1:g} * {num2:g} = {result:g}")
    elif choise == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("cannot divide by zero")
        else:
            result = num1 / num2
            print(f"Result: {num1:g} / {num2:g} = {result:g}")
    elif choise == "5":
        break
    else:
        print("Invalid choise")


#exe 19
import time
def sleep(Time):
    time.sleep(Time)
list = []
count = 0
while True:
    names = input("write a name (type 'stop' to end): ")
    if names == "stop":
        count += 0
    elif names != "stop":
        count += 1
        list.append(names)
    if names == "stop":
        break
print(f'you entered {count} names')
sleep(1)
print(list)
sleep(1)
print(f"the names in reverse order: {list[::-1]}")
sleep(1)
print(f"the names sorted alphabeticaly: {sorted(list)}")
sleep(1)


#exe 20
n = int(input("Enter a number: "))
sum_numbers = 0
for i in range(1, n+1):
    sum_numbers += i
print("Sum:", sum_numbers)
product = 1
for i in range(1, n+1):
    product *= i
print("Product:", product)


#exe 21
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))
word_count = {}
for word in words:
    word_lower = word.lower()
    if word_lower in word_count:
        word_count[word_lower] += 1
    else:
        word_count[word_lower] = 1
print("Word frequencies:")
for word, count in word_count.items():
    print(word, ":", count)


#exe 22
sentence = input("Enter a sentence: ")
words = sentence.split()

longest = words[0]
shortest = words[0]
count_long = 0

for word in words:
    if len(word) > len(longest):
        longest = word

    if len(word) < len(shortest):
        shortest = word

    if len(word) > 5:
        count_long += 1

print("Longest word:", longest)
print("Shortest word:", shortest)
print("Words longer than 5 letters:", count_long)



#exe 23
attempts = 10
numbers = []
while attempts != 0:
    num = input(f"enter 1 number, {attempts} numbers left to write")
    if num.isdigit() == False and (num[0] != "-" or num[1:].isdigit() == False):
        print("you need to enter a number")
        continue
    elif num == "" or num.isspace():
        print("you need to enter a number")
        continue
    else:
        num = int(num)
    attempts -= 1
    if int(num) >= 50:
        numbers.append(num)
print(f"the sum of the numbers you wrote that are above 50: {sum(numbers)}")


#exe 24
player_gold = 150
player_debt = 0
def update_debt(update_amount):
    global player_debt
    player_debt = player_debt + update_amount

def buy_item(item_cost):
    global player_gold
    playe_gold = player_gold - item_cost

def can_buy_item(player_gold, item_cost):
    global player_debt
    if player_gold >= item_cost + player_debt:
        return True
    else:
        return False

item_a_cost = 70
item_b_cost = 100

print(f"you have {player_gold} gold")

if can_buy_item(player_gold, item_a_cost):
    buy_item(item_a_cost)

print(f"you have {player_gold} gold")


#exe 25
def sum_digit(num: int):
    result = 0
    num = str(num)
    for digit in num:
        result += int(digit)
    return result
print(sum_digit(333))



#exe 26
def func(string):
    str_split = string.split()
    return len(str_split)
print(func("berco hagever"))


#exe 27
