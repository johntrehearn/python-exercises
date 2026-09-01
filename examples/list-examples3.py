names =[]

print(names) # prints the names in the list
names.append("Viivi") # adds the name to the end of the list
print(names) # prints the names in the list
names.append("Ahmed") # adds the name to the end of the list
print(names) # prints the names in the list
names.append("Pekka") # adds the name to the end of the list
print(names) # prints the names in the list

ahmed_index = names.index("Ahmed") # gets the index of the name in the list
print(ahmed_index) # prints the index of the name in the list

names.remove("Ahmed") # removes the name from the list
print(names) # prints the names in the list'


names.insert(1, "Olga 1") # adds the name to the list at index 1
print(names) # prints the names in the list
names.insert(100, "Olga 100") # adds the name to the list at index 100

# we cannot trust the name of the index as the index can be different at a differnt execution time of the code
# as we have added and removed names from the list so we need to get the index of the name in the list before we can remove it from the list
olga_index = names.index("Olga 1") # gets the index of the name in the list
print(olga_index) # prints the index of the name in the list
names.remove("Olga 1") # removes the name from the list
print(names) # prints the names in the list

names.extend(["Mary", "John", "Jane"]) # adds the names to the end of the list
print(names) # prints the names in the list
#does not need to be harcoded - it can be a variable that is a list of names that you want to add to the end of the list
new_names = ["Alice", "Bob", "Charlie"]
names.extend(new_names)
print(names) # prints the names in the list

names.extend(names) # adds the names to the end of the list
print(names) # prints the names in the list

if "John" in names: # checks if the name is in the list
    print("John is in the list") # prints if the name is in the list

names.sort() # sorts the names in the list in alphabetical order
print(names) # prints the names in the list