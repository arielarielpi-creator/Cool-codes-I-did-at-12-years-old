#some of the codes here were programmed with the help of ChatGPT


#exe 1
import tkinter as tk
# נפתור משוואה עם נעלם יחיד
# Solve an equation with a single variable of the form ax + b = c
def solve_linear_equation(equation):
    # ננקה רווחים מהמחרוזת
    # Remove spaces from the string
    equation = equation.replace(" ", "")
    # בשלב זה נניח שהמשוואה תמיד מהצורה "ax + b = c"
    # Assuming no spaces and always in the form "ax + b = c"
    # נמצא את מיקום ה-x כדי לטפל באורכי מקדמים משתנים
    # Find the position of 'x' to handle variable coefficient lengths
    x_index = equation.find("x")
    # נמצא את מיקום הסימן '='
    # Find the position of the '=' sign
    equal_index = equation.find("=")
    a = int(equation[:x_index])  # Coefficient of x המקדם של
    b = int(equation[x_index + 2 : equal_index])  # Constant term הערך הקבוע
    c = int(equation[equal_index + 1 :])  # Other constant term הערך הקבוע השני
    # נשתמש בנוסחה לפתרון המשוואה
    # Use the formula to solve the equation
    x = (c - b) / a
    x = round(x, 2)
    if x.is_integer():
        x = int(x)
    # נחזיר את הפתרון
    # Return the solution
    return x
root = tk.Tk()
root.title("Equation Solver")
root.geometry("800x600")
# Add widgets to each tab (parent them to the specific tab frame)
# Tab 1: Simple Equation
linear_equation_label = tk.Label(root, text="Write an equation (e.g., '2x + 3 = 7'):")
linear_equation_label.pack(pady=20)
linear_equation_entry = tk.Entry(root)
linear_equation_entry.pack(pady=10)
linear_equation_solution = tk.Label(root, text="")
def handle_solve_linear_equation(equation):
    try:
        x = solve_linear_equation(equation)
        linear_equation_solution.config(text=f"Solution: x = {x}", foreground="black")
    except Exception as e:
        linear_equation_solution.config(text=f"Error: {str(e)}", foreground="red")
linear_equation_button = tk.Button(
    root,
    text="Solve",
    command=lambda: handle_solve_linear_equation(linear_equation_entry.get()),
)
linear_equation_button.pack(pady=10)
linear_equation_solution.pack(pady=10)
root.mainloop()


#exe 2
# import time
# import pyautogui as pg
# import webbrowser as wb
# time.sleep(5)
# position = pg.position()
# print(f"X, Y = {position.x}, {position.y}")
import time
import pyautogui as pg
time.sleep(1)
pg.hotkey('win', 'd')
X, Y = 381, 755 
pg.moveTo(X, Y, duration=1)
pg.doubleClick(X, Y)
X, Y = 786, 1066
pg.moveTo(X, Y, duration=1)
pg.click(X, Y)
time.sleep(1)
pg.write("https://youtube.com", interval=0.09)
pg.press('enter')
time.sleep(3)
pg.hotkey('f11')
time.sleep(3)
X, Y = 1576, 70
pg.moveTo(X, Y, duration=1)
pg.click(X, Y)
pg.write("clash royale", interval=0.02)
pg.press('enter')
time.sleep(3)
X, Y = 988, 779
pg.moveTo(X, Y, duration=1)
pg.click(X, Y)
time.sleep(3)
X, Y = 1431, 805
pg.moveTo(X, Y, duration=1)
pg.click(X, Y)
time.sleep(3)
X, Y = 2060, 931
pg.moveTo(X, Y, duration=1)
pg.click(X, Y)
time.sleep(3)
X, Y = 1975, 1042
pg.moveTo(X, Y, duration=1)
pg.click(X, Y)
time.sleep(3)
X, Y = 2134, 1239
pg.moveTo(X, Y, duration=1)
pg.click(X, Y)
time.sleep(3)
pg.hotkey('f')


#exe 3
import itertools as it
import string

while True:
    secret = input("enter secret code (1-2 characters):\n")
    lengse = len(secret)

    if not 1 <= lengse <= 2:
        print("code length must be between 1 and 2")
        continue

    if secret.isdigit():
        for code in range(10 ** lengse):
            attempt = str(code).zfill(lengse)
            print(attempt)
            if attempt == secret:
                print(f"I successfully cracked your code, the code was: {attempt}")
                break
        break
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
        for combo in it.product(chars, repeat=lengse):
            attempt = "".join(combo)
            print(attempt)
            if attempt == secret:
                print(f"I successfully cracked your code, the code was: {attempt}")
                break
        break


#exe 4
import time
dict = {
"names": ["ariel", "liran", "ilay", "maor"],
"numbers": {
    "little": [12, 21, 67, 3],
    "big": [5735, 6003, 1555, 842]
},
"cars": ["lamborghini", "ferrari", "porsche"]
}

old_names = dict["names"][:]
old_little = dict["numbers"]["little"][:]
old_big = dict["numbers"]["big"][:]
old_cars = dict["cars"][:]

for item in dict:
    for value in dict[item],:
        time.sleep(1)
        print(item, ":", value)

print()
time.sleep(1)
print("now the new list will appear:")
print()
time.sleep(1)


dict["names"] = [name.upper() for name in dict["names"]]
dict["numbers"]["little"] = [number*3 for number in dict["numbers"]["little"]]
dict["numbers"]["big"] = [i // int(str(i)[-1]) for i in dict["numbers"]["big"]]
dict["cars"] = [dict["cars"][1], dict["cars"][-1], dict["cars"][0]]
for item in dict:
    for value in dict[item],:
        time.sleep(1)
        print(item, ":", value)

print("\nthe changes were:")
time.sleep(1)
print("Names: ", old_names, "→", dict["names"])
print("the names became names written in capital letters")
print()
time.sleep(1)
print("Little: ", old_little, "→", dict["numbers"]["little"])
print("the numbers were multiplied by 3")
print()
time.sleep(1)
print("Big: ", old_big, "→", dict["numbers"]["big"])
print("the numbers were divided by their first digit")
print()
time.sleep(1)
print("Cars: ", old_cars, "→", dict["cars"])
print("The cars changed their order randomly")


#exe 5
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


#exe 6
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


#exe 7
