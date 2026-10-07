numbers = []

for i in range(7):
    num = int(input("Enter an integer: "))
    numbers.append(num)

smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

    if num > largest:
        largest = num

print("Smallest:", smallest)
print("Largest:", largest)