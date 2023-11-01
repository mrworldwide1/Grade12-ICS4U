import math
from pcinput import getInteger

# Python Assignment 5
# In these exercises you write functions. Of course, you should not only write the functions,
# you should also write code to test them. For practice, you should also comment your func-
# tions as explained above.


# Exercise 8.1 Create a function that gets a number as parameter, and then prints the mulitiplication table for that number from 1 to 10.
# E.g., when the parameter is 12, the first line printed is “1 * 12 = 12” and the last line printed is “10 * 12 = 120.”

# function that inputs number and prints multiplication table for it
def multiTable(num):
    # multiply specified number by an incrementing i value
    for i in range(10):
        print(f"{i+1} * {num} = {(i+1)*num}")

# test function
multiTable(12)


# Exercise 8.2 Write a function that gets as parameters two strings. The function returns
# the number of characters that the strings have in common. Each character counts only once,
# e.g., the strings "bee" and "peer" only have one character in common (the letter “e”). You
# can consider capitals different from lower case letters. Note: the function should return the
# number of characters that the strings have in common, and not print it. To test the function,
# you can print the result in your main program.

# takes in two strings and return number of characters that both have in common
def commonChar(a, b):
    letters = []
    commonLetters = []
    commonNum = 0
    
    # add common letters to list and increment sum
    for char in "abcdefghijklmnopqrstuvwxyz":
        if (char in a and char in b) and (char not in commonLetters):
            commonLetters.append(char)
            commonNum += 1
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if (char in a and char in b) and (char not in commonLetters):
            commonLetters.append(char)
            commonNum += 1
    return commonNum

# test function
print(commonChar("bee", "pear"))
print(commonChar("Eren", "Yeager"))


# Exercise 8.3 The Grerory-Leibnitz series approximates pi as 4 ∗ (1/1 − 1/3 + 1/5 − 1/7 +
# 1/9...). Write a function that returns the approximation of pi according to this series. The
# function gets one parameter, namely an integer that indicates how many of the terms between the parentheses must be calculated.

# def piSeries(termAmount):
#      amount = 1
#      term = 1/amount
#      for i in range(termAmount):
#          term = 1/(amount+2)
#      approx = 4 * 


# Exercise 8.4 
# In Chapter 6 you were asked to implement the quadratic formula to solve quadratic equations. A quadratic equation is described by three numeric values, usually
# called A, B, and C. It has zero, one, or two solutions, depending on the discriminant (the part
# under the square root). Write a function that solves a quadratic equation. As parameters it
# gets A, B, and C. It returns three values. The first is an integer that indicates the number
# of solutions. The second is the first solution. The third is the second solution. Any of the
# solutions that do not exist, you can return as zero.

# function to solve quadratic equation taking in each term as parameter
def quadSolve(A, B, C):

    # calculate discriminant
    discrim = (B**2)-4*(A)*(C)

    # check value of discriminant and output answers accordingly
    if discrim == 0:
        numSolutions = 1
        # formula for x-coord of vertex
        firstSolution = (-B) / (2*A)
        secondSolution = 0
    elif discrim > 0:
        numSolutions = 2
        firstSolution = (-B + math.sqrt(B**2 - 4*A*C)) / (2*A)
        secondSolution = (-B - math.sqrt(B**2 - 4*A*C)) / (2*A)
    elif discrim < 0:
        numSolutions = 0
        firstSolution = 0
        secondSolution = 0

    return(f"Number of solutions: {numSolutions}, first solution: {firstSolution}, second solution: {secondSolution}")

print(quadSolve(-1, 3, -5))

# Exercise 8.5 In Chapter 7, the loop-and-a-half was explained. The final code for the ex-
# ample that was presented is given below, and I made the remark that there is still something
# ugly about this code, namely the fact that if x is smaller than zero or higher than 1000, the
# code still asks for y even when it can know that it has to ask a new value for x. I also re-
# marked that you can resolve this in an easy way by using a function. Create a function and
# insert it in this code, so that this issue gets fixed. Also get rid of the exit() and thus the
# possible ugly output by introducing a main() function.

# no need to create a new function. I just added a conditional to the pcinput getinteger function
# to ask for new num if its <0 or >1000.
def main():
  while True:
    x = getInteger("Enter number 1: ")
    if x == 0:
      break
    y = getInteger("Enter number 2: ")
    if y == 0:
      break
    if x%y == 0 or y%x == 0:
      print("Error: the numbers cannot be dividers")
      return
    print(f"Multiplicaiton of {x} and {y} gives {x*y}")
  print("goodbye!")

if __name__ == '__main__':
  main()


# Exercise 8.7 - What is wrong with the following code? Fix it!

# def area_of_triangle(bottom, height):
#     area = 0.5 * bottom * height
#     print( "The area of a triangle with a bottom of", bottom,
#     "and a height of", height, "is", area )
# print( area_of_triangle( 4.5, 1.0) )

# In the code above, inside the function should return the area instead of printing it.
# in its current state, printing the result of calling the function results in a recursion error. Also its best practice to return values
# rather than using print() within functions.

# Fixed version:
def area_of_triangle(bottom, height):
    area = 0.5 * bottom * height
    return("The area of a triangle with a bottom of", bottom, "and a height of", height, "is", area)
print(area_of_triangle(4.5, 1.0))