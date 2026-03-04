import json
import os

# Path to our data file
FILE_PATH = "data/database.json"

def save_db(data):
    # Make the data folder if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Write the whole dictionary to the JSON file
    with open(FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)

def load_db():
    # If the file isn't there, return empty lists so the app doesn't crash
    if not os.path.exists(FILE_PATH):
        return {"users": [], "projects": [], "tasks": []}
    
    # Read the data back into Python
    with open(FILE_PATH, 'r') as f:
        return json.load(f)