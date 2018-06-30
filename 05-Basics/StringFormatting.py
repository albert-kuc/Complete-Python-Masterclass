"""
27. String Formatting - Displaying Numbers and Strings

Example of using replacement fields
"""

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))

print(30*"-")

for i in range(1, 12):
    print("No. {0:<2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))

print(30*"-")

print("Pi is approximately {0:12.50}".format(22/7))
