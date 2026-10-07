def change_string(s):
    s = "X" + s[1:]
    print("Inside function:", s)

my_string = "Hello"

change_string(my_string)

print("Outside function:", my_string)