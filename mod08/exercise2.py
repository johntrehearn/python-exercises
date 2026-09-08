names = set()

name = input("Enter name: ")

while name != "":
    if name in names:
        print("Existing name")
        name = input("Enter name: ")
    else:
        names.add(name)
        print("New name.")
        name = input("Enter name: ")

print("The list of names is:")
for name in names:
    print(name)