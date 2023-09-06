import numpy

numbers = []

print("This program will generate a defined number of random numbers without repetition in a defined range")
print("After a number is printed you must press enter for the next number to print")

startingNumber = int(input("What is the smallest number in the range? "))
finalNumber = int(input("What is the largest number on the range? "))
numNumbers = int(input("How many numbers should be generated? "))

# if more numbers are requested than are in the range, a number must be repeated
# - 1 is necessary to include both top and bottom numbers
while numNumbers - 1 > finalNumber - startingNumber:
    print("That many numbers cannot be generated")
    numNumbers = int(input("How many numbers should be generated? "))

for i in range(numNumbers):
    number = numpy.random.randint(startingNumber, finalNumber + 1)
    lock = 0
    while lock == 0:
        if number in numbers:
            number = numpy.random.randint(startingNumber, finalNumber + 1)
        else:
            lock = 1
    numbers.append(number)
    print(numbers[i])
input("")
