# FOR Loop Exercise
# Write a program to print/display the multiplication tables of a specific number between 0 and 13
# the b) for all number between 0 and 13.
# Oct 18, 2023
# Lucas Leung

# print multiplication table of specific number between 0-13
specificNum = 10
print(f"Multiplication table for {specificNum}:")

for i in range(14):
    print(f"{specificNum}*{i} = {(i)*specificNum}")

print('-------------------------------------------------')

# for all numbers between 0-13
for number in range(14):
    print(f"Multiplication table for {number}:")
    for digit in range(14):
        print(f"{number}*{digit} = {(digit)*number}")