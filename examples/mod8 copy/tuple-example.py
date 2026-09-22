days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print("Days of the week:", days_of_the_week)
print("The first day of the week is:", days_of_the_week[0])
print("The last day of the week is:", days_of_the_week[-1])
print("The days of the week in reverse order are:", days_of_the_week[::-1])
print("The days of the week from Wednesday to Friday are:", days_of_the_week[2:5])
print("The days of the week from Monday to Thursday are:", days_of_the_week[:4])

print(len(days_of_the_week), "days in a week.")
print(len((1, 2, 3, 4, 5)), "numbers in a tuple.")
print(days_of_the_week.count("Monday"), "occurrences of Monday in the tuple.")

print("The index of Wednesday in the tuple is:", days_of_the_week.index("Wednesday"))

# no way to change the value of a tuple, but you can create a new tuple with the desired changes
# if you try to access something that is out of range, you will get an IndexError:tupe indes out of range


day_number = int(input("Enter the day number (1-7): "))
day = days_of_the_week[day_number-1]
print(f"Day number {day_number} is {day}.")
#print(days_of_the_week[10])  # This will raise an IndexError: tuple index out of range
print(len(days_of_the_week) > 10)

#this tuple may come from a database or an API, and you may not know the length of it, so you should always check the length before accessing an index that may be out of range 
if 1 <= day_number <= len(days_of_the_week):
    day = days_of_the_week[day_number-1]
    print(f"Day number {day_number} is {day}.")

#You can use for in loops to iterate through the elements of a tuple, and you can use the len() function to get the length of a tuple. You can also use the index() method to find the index of an element in a tuple, and you can use the count() method to count the occurrences of an element in a tuple. You can also use slicing to get a subset of a tuple, and you can use negative indexing to access elements from the end of a tuple.

for day in days_of_the_week:
    print(day)

# you can use the in operator to check if an element is in a tuple, and you can use the not in operator to check if an element is not in a tuple. You can also use the + operator to concatenate two tuples, and you can use the * operator to repeat a tuple a certain number of times. You can also use the min() and max() functions to find the minimum and maximum elements in a tuple, and you can use the sum() function to find the sum of the elements in a tuple.
if "Monday" in days_of_the_week:
    print("Monday is in the tuple.")