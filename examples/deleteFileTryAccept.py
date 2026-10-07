# to delete a file you must use the OS package

import os

try:
    with open("save.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error while handling the file.")

