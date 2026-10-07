import json

save_data = {
    "film": "Star Wars",
    "year": "1991",
    "actors": ["Terry", "Mike", "Peter"]
    }

with open("filmJSON.json", "w") as file:
   json.dump(save_data, file)

with open("filmJSON.json", "r") as file:
   movie_data = json.load(file)
   print(f"Name: {movie_data["film"]}")
   print(f"Year: {movie_data["year"]}")
   print(f"Actors: {movie_data["actors"]}")