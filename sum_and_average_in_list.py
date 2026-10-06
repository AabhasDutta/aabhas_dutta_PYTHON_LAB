numbers = []
total = 0

for i in range(10):
    num = int(input("Enter an integer: "))
    numbers.append(num)
    total = total +  num

average = total / 10

print("List:", numbers)
print("Sum:", total)
print("Average:", average)
