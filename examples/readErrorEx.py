import os

try:
    with open("beer.txt", "r") as my_file:
        file_data = my_file.read()
except FileNotFoundError as e:
    print("File not found")
except IOError as e:
    print("An error occurred")
    print(e)