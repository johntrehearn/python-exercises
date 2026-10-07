# to delete a file you must use the OS package

import os

if os.path.exists("save.txt"):
    print("File Exits")
    os.remove("save.txt")
    print("File Deleted")