numbers = []

n = int(input("How many integers do you want to enter? "))

for i in range(n):
    num = int(input("Enter an integer: "))
    numbers.append(num)

reversed_list = []

for i in range(n - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reversed_list)