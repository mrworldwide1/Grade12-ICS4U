## CodersA-Ch-3-Exercises.pdf

# Exercise 3.1
# The cover price of a book is $24.95, but bookstores get a 40 percent discount.
Shipping costs $3 for the first copy and 75 cents for each additional copy. Calculate the total
wholesale costs for 60 copies.

# Book cover price
coverPrice = 24.95

# Bookstore discount
discount = 0.60

# Price of book for bookstore
firstCopyShipping = 3
addtlCopyShipping = 0.75
copies = 60

def wholeSaleCost(coverPrice, discount, copies, firstShippingCost, addtlShippingCost):
  bookStore
  
return wholeSaleCosts


# Exercise 3.2
# Can you identify and explain the errors in the following lines of code? Correct them.=
# exercise0302.py
# print( "A message" ).
# print( "A message ' )
# print( ' A messagef" ' )

# The first line's error is that there is a period after the closing bracket
print("A message")

# The second line uses a quote and apostrophy around the input but only one type can be used
print('A message')

# The third line's f-string is placed in the incorrect place, it must before the input and only one type of quotes can be used
print(f"A message")
