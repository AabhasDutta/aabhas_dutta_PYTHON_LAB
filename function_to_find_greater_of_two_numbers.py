def maximum(a, b):
    if a > b:
        return a
    else:
        return b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = maximum(num1, num2)

print("The greater number is:", result)