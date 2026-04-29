user_input = input("Enter something: ")
def func(string):
    str_split = string.split()
    return len(str_split)
print(func(user_input))