#You can have nested tuples, which are tuples that contain other tuples as elements. For example:
nested_tuple = (1, 2, (3, 4), (5, 6, (7, 8)))
print("Nested tuple:", nested_tuple)

# there can be boolean values in a tuple, and they can be used in conditional statements. For example:
bool_tuple = (True, False, True)
if bool_tuple[0]:
    print("The first value in the tuple is True.")  
#they can contain other data types, such as strings, integers, floats, and even other tuples. For example:
mixed_tuple = ("hello", 42, 3.14, True, (1, 2, 3))
print("Mixed tuple:", mixed_tuple)

#accessing nested tuples can be done using multiple indices. For example, to access the value 4 in the nested_tuple above, you would use nested_tuple[2][1]. This is because the value 4 is located in the second element of the nested tuple (3, 4), which is itself the third element of the outer tuple.

#index
value = nested_tuple[2][1]
print("The value at index [2][1] in the nested tuple is:", value)   
#getting the item inside a nested tuple can be done using multiple indices. For example, to get the value 8 in the nested_tuple above, you would use nested_tuple[3][2][1]. This is because the value 8 is located in the second element of the innermost tuple (7, 8), which is itself the third element of the outer tuple (5, 6, (7, 8)), which is itself the fourth element of the outermost tuple (1, 2, (3, 4), (5, 6, (7, 8))).
#getting the item inside a nested tuple can be done using multiple indices. For example, to get the value 8 in the nested_tuple above, you would use nested_tuple[3][2][1]. This is because the value 8 is located in the second element of the innermost tuple (7, 8), which is itself the third element of the outer tuple (5, 6, (7, 8)), which is itself the fourth element of the outermost tuple (1, 2, (3, 4), (5, 6, (7, 8))).

value = nested_tuple[3][2][1]
print("The value at index [3][2][1] in the nested tuple is:", value)    

print(nested_tuple[3][2][1])  # This will print 8   


value5 = ((1, 2), (3, 4), (5, 6, (7, 8, (9, 10))))
print("The value at index [2][2][1] in the nested tuple is:", value5[2][2][1])  # This will print 10

#Lists are mutable, meaning that you can change their contents after they are created. Tuples, on the other hand, are immutable, meaning that once they are created, their contents cannot be changed. This means that you cannot add, remove, or change elements in a tuple after it is created. However, you can create a new tuple that contains the desired changes.
#but lists are mutiple even if they are in a tuple


