names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary", 1, 2, False, True, [], [1,2,3], ["a", "b", "c"]]
#normally easier to work with it if there is only one data type in the list/array but it is possible to have multiple data types in a list
# in other programing languages the list is called an array and it is not possible to have multiple data types in an array

empty_list = [] # you can create an empty list by using empty square brackets whcih you can populate later
print(empty_list)
print(empty_list)

print(names[0])  # prints the first name in the list
print(names[1])  # prints the second name in the list

print(len(names))  # prints the number of names in the list
print(len([])) # prints the number of names in the list

print(names[4])  # prints the 4th name in the list
print(names[-2])  # prints the second-to-last name in the list

print(names[1:3])  # prints the names from index 1 to 2 IT DOES 
                     # NOT INCLUDE THE LAST ITEM not inclusive
print(name[0:2+1]) # prints the names from index 0 to 2 inclusive

print(name[0:5]) # prints the names from index 0 to 4 inclusive
print(name[0:5:2]) # prints the names from index 0 to 4 inclusive with a step of 2

print (names[1:-1]) # prints the names from index 1 to the second-to-last name in the list

print(names[2:]) # prints the names from index 2 to the end of the list
print(names[:3]) # prints the names from the beginning of the list to index 2 inclusive

print(names)
names.reverse() # reverses the order of the names in the list
print(names) #The index location of the names in the list has changed after reversing the list (not stored in the original array it is the order that they are now in)

#len gives you the number of items in the list. The index of the last item in the list is always one less than the length of the list. For example, if a list has 5 items, the index of the last item is 4.

if len(names) > 5:
    print(names[5])  # This will not be executed because the length of names is not greater than 5 
