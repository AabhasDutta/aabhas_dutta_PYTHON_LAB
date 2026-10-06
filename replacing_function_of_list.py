#question 1
# Create a list of 5 fruits

fruits = []

for i in range(5):
    fruit = input("Enter a fruit: ")
    fruits.append(fruit)  


    
print("2nd item=",fruits[1])
print("4th item =",fruits[3])

fruits[4]="mango"
print("updated list=", fruits)


