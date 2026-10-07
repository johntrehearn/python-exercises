import os

try:
    os.remove("movie.json")
except Exception as e:
    print(e)
