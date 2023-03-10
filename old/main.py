# This is a sample Python script.
"""
print("Hello, world!")
print(100 + 10 + 2.5)
print(22 * 3)
print(15 - 75)
print(6 / 3)
print(7 // 3)
print(7 % 3)

a = 2
b = 3
c = "ABCEDar"
d = 4.5
print(a, b, c, d)

a = input("Introduceti un numar")
print(a * 5)
a = int(a)
print(a * 5)




name = input("Introduceti prenumele")
surname = input("Introduceti numele")
print("Hello", name, surname)


'''
This is a multi-line comment.
This line will be ignored
'''

# This line will be ignored
"""
import sys

"""
Bigger comments can be written
over multiple lines.
This is a multi-line comment.
"""
"""
print("Py loves Python")

# Bigger comments can be written
# over multiple lines.
# This is a multi-line comment.

a = 5
b = 10.0
c = a + b
print(c) # Output: 15.0


a = 10
b = 5
c = a / b
print(c) # Output: 2.0


a = "Hello"
b = "world"
c = a + b
print(c) # Output: "Helloworld"

a = 5.0
b = 5
print(a == b) # Output: True



print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

print("The itsy bitsy spider" , "climbed up" , "the waterspout.")


print("My name is", "Python.", end=" ")
print("Monty Python.")

print("My", "name", "is", "Monty", "Python.", sep="-")

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")


print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")


print(0o123)

print(0x123)

print(0.4)
print(4.)
print(.1)

print(True)
print(False)

print(True > False)
print(True < False)


a = 10
print(type(a))
print(a)

a = 3.14
print(type(a))
print(a)

number = 6.9999999
number = int(number)
print(number)


a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

patterns = [
    ["###", "# #", "# #", "# #", "###"],  # 0
    ["  #", "  #", "  #", "  #", "  #"],  # 1
    ["###", "  #", "###", "#  ", "###"],  # 2
    ["###", "  #", "###", "  #", "###"],  # 3
    ["# #", "# #", "###", "  #", "  #"],  # 4
    ["###", "#  ", "###", "  #", "###"],  # 5
    ["###", "#  ", "###", "# #", "###"],  # 6
    ["###", "  #", "  #", "  #", "  #"],  # 7
    ["###", "# #", "###", "# #", "###"],  # 8
    ["###", "# #", "###", "  #", "###"],  # 9
]

def display_digit(num):
    digits = [int(d) for d in str(num)] # convert number to list of digits
    rows = [""] * 5 # initialize the rows to empty strings
    for digit in digits:
        pattern = patterns[digit] # get the pattern for the current digit
        for i, row in enumerate(pattern):
            rows[i] += row + " " # add the current row to the corresponding row of the display
    for row in rows:
        print(row) # print the final display

# example usage:
display_digit(123) # prints the number 123 using the LED display
"""