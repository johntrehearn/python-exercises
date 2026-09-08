number_list = [1, 2, 3, 4, 5]

def sum_of_list(number_list):
    listLength = len(number_list)
    sumOfList = 0
    for i in range(listLength):
        sumOfList += number_list[i]
    return sumOfList

print("The sum of the numbers in the list is:", sum_of_list(number_list))