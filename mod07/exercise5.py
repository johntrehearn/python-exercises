original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_even_numbers(original_list):
    print("Original list:", original_list)
    filtered_list = []
    for number in original_list:
        if number % 2 == 0:
            filtered_list.append(number)
    print("List with even numbers only:", filtered_list)
    return filtered_list


filter_even_numbers(original_list)