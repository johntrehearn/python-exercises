

games ={"Monopoly", "Chess", "Checkers", "Scrabble", "Clue", "Risk", "Catan"}

print(games)
print(games)
print(games)
print(games)
print(games)
print(games)

# the order changes every time you run the program because sets are unordered collections of unique elements. When you print a set, the elements are displayed in a random order, which can vary each time the program is executed. This is because sets do not maintain any specific order for their elements, unlike lists or tuples.
#we don't know the order of the elements in a set, and it can change every time we run the program. This is because sets are implemented using hash tables, which do not guarantee any specific order for the elements. The order of the elements in a set is determined by the hash values of the elements, which can vary depending on the implementation and the input data. Therefore, when we print a set, we may see the elements in a different order each time we run the program.
#but we dont'care about the order of the elements in a set, we just want to know what elements are in the set. The order of the elements in a set is not important, as long as we can access the elements we need.

#print(game(0)) # This will raise an error because sets do not support indexing. You cannot access elements in a set using an index like you can with lists or tuples. Sets are unordered collections, so there is no concept of an "index" for their elements. If you need to access elements by index, you should use a list or tuple instead.

#games. there are so many more option here, but we don't need to know them all. We just need to know that sets are unordered collections of unique elements, and that they do not support indexing. We can use sets to store unique elements and perform set operations like union, intersection, and difference.

games.add("Uno") # adds an element to the set
games.add("Uno") # does not add a duplicate element to the set

#It will add uno at any place in the set, because sets are unordered collections of unique elements. When you add an element to a set, it is placed in a position determined by the hash value of the element, which can vary depending on the implementation and the input data. Therefore, the order of the elements in a set is not guaranteed, and you cannot predict where a new element will be added.

for i in range(60):
    games.add(f"uno") #this will not add any more elements to the set because sets only store unique elements. Since "uno" is already in the set, adding it again will have no effect. The set will still contain only one instance of "uno".

print(games)

#if you create and empty set with {} then it is not a set it is a dictionary. You can create an empty set with set() or with {} but you have to use the set() function to create an empty set. If you use {} then it will create an empty dictionary instead of an empty set.   
empty_set=set() # this is an empty set


#you can intirate through a set with a for loop, but you cannot access the elements of a set by index because sets are unordered collections of unique elements. You can use a for loop to iterate through the elements of a set, but you cannot use indexing to access specific elements. If you need to access elements by index, you should use a list or tuple instead.

for game in games:
    print(game)



games.add("Risk") # adds an element to the set

print(games)

games.remove("Risk") # removes an element from the set

print(games)

#to check if an element is in a set, you can use the in operator. For example, to check if "Chess" is in the games set, you can use the following code:
if "Chess" in games:
    print("Chess is in the games set.")
else:
    print("Chess is not in the games set.")

# remember each element in a set is unique, so if you try to add a duplicate element to a set, it will not be added. For example, if you try to add "Chess" to the games set again, it will not be added because it is already in the set.
# but it does not raise an error, it just does not add the duplicate element to the set. This is because sets are unordered collections of unique elements, and they do not allow duplicate elements. If you try to add a duplicate element to a set, it will simply be ignored and the set will remain unchanged.