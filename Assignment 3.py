import math
import random

# Exercise 5.1
# Ask the user to enter a string. Then print the length of that string. Use the
# input() function rather that the getString() function from pcinput, as the getString()
# function removes leading and trailing spaces.

print("enter a string:")
print(len(input()))

# Exercise 5.2 The Pythagorean theorem states that of a right triangle, the square of the
# length of the diagonal side is equal to the sum of the squares of the lengths of the other two
# sides (or a2 + b 2 = c2). Write a program that asks the user for the lengths of the two sides
# that meet at a right angle, then calculate the length of the third side (in other words: take
# the square root of the sum of the squares of the two sides that you asked for), and display it
# in a nicely formatted way. You may ignore the fact that the user can enter negative or zero
# lengths for the sides.

# takes in 2 known triangle side lengths and return third side length by applying pythagorean theorem
def pythag(b, c):
  return math.sqrt(b**2 + c**2)

#ask for the 2 known side lengths of right triangle
b = int(input('First side length of your right triangle: '))
c = int(input('Second side length of your right triangle: '))

#gives the answer
print('The third side length is: ' + str(pythag(b, c)))


# Exercise 5.3 Ask the user to enter three numbers. Then print the largest, the smallest, and their average, rounded to 2 decimals.

numbers = []
sum = 0

# add the 3 numbers to empty list then count the sum
for i in range (3):
    numbers.append(int(input("Enter a number: ")))
for num in numbers:
   sum += num

# print largest/smallest/average by examining list
print(f"Largest number: {max(numbers)}")
print(f"Smallest number: {min(numbers)}")
print(f"Average: {round(sum/3, 2)}")

# Exercise 5.4 Calculate the value of e to the power of -1, 0, 1, 2, and 3, and display the results, with 5 decimals, in a nicely formatted manner.

# calculate and nicely print value of e to power of -1, 0, 1, 2, 3 with 5 decimals
print(f"The value of e raised to the power of -1 is: {round(math.e**-1, 5)}")
print(f"The value of e raised to the power of 0 is: {round(math.e**0, 5)}")
print(f"The value of e raised to the power of 1 is: {round(math.e**1, 5)}")
print(f"The value of e raised to the power of 2 is: {round(math.e**2, 5)}")
print(f"The value of e raised to the power of 3 is: {round(math.e**3, 5)}")

# Exercise 5.5 Suppose you want to generate a random integer between 1 and 10 (1 and 10
# both included), but from the random module you only have the random() function available
# (you can use functions from other modules, though). How do you do that?

# The random module generates a random float between 0.1 and 1.0.
# Therefore, convert the output into an integer by multiplying by 10, and then round it, to get rid of the decimals.
# Ex. 0.47732 would become 4
randInt = round(random.random()*10)
print(randInt)
