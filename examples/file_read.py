# Open  a File

# Write mode - overwrite

with open("save_file.txt", "w") as my_file:
    my_file.write("This is a new save file")

# Append Mode

# By default it will just dump it in the file. If you want a new line you have to specify
#     my_file.write("\nThis is a new save file\n")

with open("save_file.txt", "a") as my_file:
    my_file.write("This is a new save file")

# To open in a different folder 
with open("C:\Users\JTTPM\OneDrive - Metropolia Ammattikorkeakoulu Oy\Documents\Software_1\python-exercises\examples\test_file.txt", "w") as my_file:
    my_file.write("This is a new save file")