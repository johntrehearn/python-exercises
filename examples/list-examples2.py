names = []

name = input("Enter a name, empty line to exit: ")

while names != "":
    print(len(names)) # prints the length of the name that was entered
    names.append(name)
    print(names) 

    #can type name. and then you will get a list of all the methods that you can use with the list data type such as extend list to the end
    # method that is called on the list SO YOU HAVE TO USE BRACKETS
    print(len(names)) # prints the length of the name that was entered
    name = input("Enter a name, empty line to exit: ")

    # hover and whatever after the -> is the description of the return value of the method that you are using. 

print(names) # prints the names in the list