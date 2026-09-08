# unpacking is making new variables from the contents of a tuple
# There must be the same number of new variables as there was in the tuple 

fruits = "Orange", "Banana", "Apple"
(first, second, third) = fruits

fruits = "Orange", "Banana", "Apple"
(first, second, third) = ("Orange", "Banana", "Apple")

fruits = "Orange", "Banana", "Apple"
first = "Orange"
second = "Banana"
third = "Apple"

(first, second, third) = ("Orange", "Banana", "Apple")

# when unpacking, you can use the * operator to unpack the remaining elements of a tuple into a list. For example, if you have a tuple with 5 elements and you want to unpack the first 2 elements into variables and the remaining 3 elements into a list, you can do it like this:
fruits = "Orange", "Banana", "Apple", "Grapes", "Mango"
(first, second, *remaining) = fruits

#the new variables will be on the left side of the assignment operator, and the tuple will be on the right side of the assignment operator. The * operator will unpack the remaining elements of the tuple into a list, which will be assigned to the variable on the left side of the assignment operator.
#then it means you only need to unpack the first two elements of the tuple into variables, and the remaining elements will be unpacked into a list. The list will contain the remaining elements of the tuple, which can be accessed using indexing or slicing. 
#it means you only need to update a variable once

print(f"The fruits are: {first}, {second} and {third}.")

print(first)