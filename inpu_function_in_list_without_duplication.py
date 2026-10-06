numbers = []
unique = []

n = int(input("How many integers do you want to enter? "))

for i in range(n):
    num = int(input("Enter an integer: "))
    numbers.append(num)

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique)