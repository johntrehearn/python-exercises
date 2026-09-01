number = input("Enter a number: ")

numbers = []

while number != "":
    numbers.append(int(number))  # Convert the input to an integer before appending. THIS IS WHERE YOU HAVE TO DO THE CONVERSION
    number = input("Enter a number: ")

print(numbers)

#numbers.reverse()  # Reverses the order of the list

numbers.sort(reverse=True)  # Sorts the list in descending order
print(numbers)

print(numbers [:5])  