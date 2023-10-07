## 4.1
# define variables
var1 = int(input())
var2 = int(input())
var3 = int(input())

# calculate average of 3 variables
average = (var1+var2+var3) / 3

# print average
print(f"The average of the three variables is {average}")


## 4.2
radius = 999
pi = 3.14159
print(f"The surface area of a circle with radius {radius} is... {(radius**2)*pi}")


## 4.3
# Convert dollar amount to cents
amount = 11.52
cents = amount * 100

# Calculate number of coins that can go into cents and remainder
# dollars
dollarsRemainder = cents % 100
dollars = (cents - dollarsRemainder) / 100

# quarters
quartersRemainder = dollarsRemainder % 25
quarters = (dollarsRemainder - quartersRemainder) / 25

# dimes
dimesRemainder = quartersRemainder % 10
dimes = (quartersRemainder - dimesRemainder) / 10

# nickels
nickelsRemainder = dimesRemainder % 5
nickels = (dimesRemainder - nickelsRemainder) / 5

# pennies
penniesRemainder = nickelsRemainder % 1
pennies = (nickelsRemainder - penniesRemainder) / 1

# print answer; number of coins
print(f"Dollars: {dollars}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")


## 4.4
a = 17; b = 23
a += b
# switch values by adding and subtracting difference
b = a - b
a -= b

# print answer
print(f"a = {a} b = {b}")
