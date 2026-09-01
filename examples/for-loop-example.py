names = []

name = input("Enter the first name or quit by pressing Enter: ")
while name != "":
    names.append(name)
    name = input("Enter the next name or quit by pressing Enter: ")

print(names)
"""
print(names[0])  # prints the first name in the list
print(names[1])  # prints the second name in the list

"""

for name in names:
    print(name)  # prints the name in the list

    # name is just a variable so you can do any of the thing you can do with a variable such as print the length of the name that was entered

# or

i = 0
for name in names:
    #print(names[i])  # prints the name in the list
    print(f"Value at index {i} is {name}")  # prints the name in the list

    i = i + 1          # or i += 1