import math

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

    discrim = (B**2)-4*(A)*(C)

    if discrim == 0:
        numSolutions = 1
    elif discrim > 0:
        numSolutions = 2
    elif discrim < 0:
        numSolutions = 0

    firstSolution = (-B + math.sqrt(B**2 - 4*A*C)) / (2*A)
    secondSolution = (-B - math.sqrt(B**2 - 4*A*C)) / (2*A)

    return(f"Number of solutions: {numSolutions}, first solution: {firstSolution}, second solution: {secondSolution}")

print(quadSolve(-1, 3, -5))

# Exercise 8.5 In Chapter 7, the loop-and-a-half was explained. The final code for the example that was presented is given below, and I made the remark that there is still something
# ugly about this code, namely the fact that if is smaller than zero or higher than 1000, the
# code still asks for even when it can know that it has to ask a new value for . I also re-
# marked that you can resolve this in an easy way by using a function. Create a function and
# insert it in this code, so that this issue gets fixed. Also get rid of the () and thus the possible ugly output by introducing a main () function.



# Exercise 8.6 In statistics, the binomial coefficient indexed by and (often expressed as
# “n over k,” whereby must be bigger than or equal to ) is calculated as n!/(k! ∗ (n − k)!),
# whereby n! indicates the factorial of . As I explained in Chapter 7: the factorial of a positive
# integer is that integer, multiplied by all positive integers that are lower (excluding zero). You
# write the factorial as the number with an exclamation mark after it. E.g., the factorial of 5
# is 5! = 5 ∗ 4 ∗ 3 ∗ 2 ∗ 1 = 120. If you did all the exercises until now, you wrote some code
# for this. Write a function that calculates the binomial coefficient for its two parameters, and
# returns the value. Write the code in such a way that it can be used as a module by another
# program (i.e., put the tests of your program in a () function that is called as explained
# above).

def binoCoeff(a, b):
    pass

# Exercise 8.7 - What is wrong with the following code? Fix it!

