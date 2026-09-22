#Most commonly used data structure in Python is the dictionary. A dictionary is a collection of key-value pairs, where each key is unique and maps to a value. Dictionaries are mutable, meaning you can change their contents after they are created. They are also unordered, meaning the order of the key-value pairs is not guaranteed.

#it is core value to know how to use dictionaries in Python, as they are used in many different applications and libraries. Dictionaries are used to store data in a way that allows for fast lookups and efficient storage. They are also used to represent complex data structures, such as JSON objects, which are commonly used in web development. 

#Dictionaries are also used in many different libraries and frameworks, such as Django, Flask, and Pandas. In Django, dictionaries are used to represent database models and querysets. In Flask, dictionaries aka associative table, associative array, hash table, hash map, or symbol table are used to represent request and response objects. In Pandas, dictionaries are used to represent data frames and series.    

#The key is a unique identifier for a value in the dictionary. The value can be any data type, including another dictionary. Dictionaries are created using curly braces {} and key-value pairs are separated by colons. For example, a simple dictionary that maps names to ages can be created like this:
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}

#but there are only 3 values as they ksya re a value pair. It is not a variable, it is a data structure that holds key-value pairs. The keys are unique and the values can be any data type. You can access the values in a dictionary using the keys, like this:
print(ages["Alice"]) # prints 30

numbers = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}

numbers["Olga"] = "050-1011012"
numbers["Mary"] = "0401-2132139"

print(numbers)

name = input("Enter name: ")
if name in numbers:
    print(f"{name}'s phone number is {numbers[name]}.")

print(numbers("Viivi")) # prints 050-1234567
print(numbers("ahmed")) # gives "Key Error"
#as you can see, the keys are case-sensitive, so "Ahmed" and "ahmed" are considered different keys. If you try to access a key that does not exist in the dictionary, you will get a KeyError. You can use the get() method to avoid this error and return a default value instead. For example:

if "ahmed" in numbers:
    print(f"Ahmed's phone number is {numbers.get('ahmed', 'not found')}.")

if "Ahmed" in numbers:
    print(f"Ahmed's phone number is {numbers.get('Ahmed', 'not found')}.")

#There are no indexes in a dictionary, so you cannot access the values using an index like you can with a list or tuple. You can only access the values using the keys. If you need to access the values in a specific order, you can use the items() method to get a list of key-value pairs and then sort that list. For example:

# name[0] won't work, as there are no indexes in a dictionary. You can only access the values using the keys. If you need to access the values in a specific order, you can use the items() method to get a list of key-value pairs and then sort that list. For example:
#keys can be strings, numbers, or tuples, but they must be immutable. Values can be any data type, including lists, dictionaries, and even other dictionaries. You can also use the del statement to remove a key-value pair from a dictionary. For example:
del numbers["Pekka"]
print(numbers)
#but it is easier if you stringify the key, as it is easier to read and understand. You can also use the pop() method to remove a key-value pair from a dictionary and return the value. For example:

for item in numbers.items():
    print(item)
    print(f"{item[0]}'s phone number is {item[1]}.")

numbers.add("Pekka", "050-7654321") # adds a key-value pair to the dictionary

numbers.update({"Pekka": "050-7654321"}) # adds a key-value pair to the dictionary
numbers.pop("Pekka") # removes a key-value pair from the dictionary and returns the value
numbers.pop("Pekka", "not found") # removes a key-value pair from the dictionary and returns the value, or "not found" if the key does not exist
numbers.clear() # removes all key-value pairs from the dictionary

#inspect and iterate in the same way

for number in numbers:
    print(f"{number}'s phone number is {numbers[number]}.")

for name, number in numbers.items():
    print(f"{name}'s phone number is {number}.")

for name in numbers.keys():
    print(f"{name}'s phone number is {numbers[name]}.")

#if you need the value use the values() method to get a list of all the values in the dictionary. For example:

for number in numbers.values():
    print(f"Phone number is {number}.")

# a dictionary can be used to store data in a way that allows for fast lookups and efficient storage. They are also used to represent complex data structures, such as JSON objects, which are commonly used in web development. Dictionaries are also used in many different libraries and frameworks, such as Django, Flask, and Pandas. In Django, dictionaries are used to represent database models and querysets. In Flask, dictionaries are used to represent request and response objects. In Pandas, dictionaries are used to represent data frames and series.
#they are not normally ordered

#Nested Data Structures: Dictionaries can also be nested, meaning that a dictionary can contain another dictionary as a value. This allows for the creation of complex data structures that can represent real-world objects and relationships. For example, a dictionary that represents a person could contain another dictionary that represents their address, which in turn could contain another dictionary that represents their city and state.
person = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA"
    }
}