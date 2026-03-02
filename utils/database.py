import json
import os

DB_PATH = "data/database.json"

def save_db(data):
    """Saves the dictionary to a JSON file."""
    if not os.path.exists("data"):
        os.makedirs("data")
    with open(DB_PATH, 'w') as f:
        json.dump(data, f, indent=4)

def load_db():
    """Loads data or returns a blank template."""
    if not os.path.exists(DB_PATH):
        return {"users": [], "projects": [], "tasks": []}
    with open(DB_PATH, 'r') as f:
        return json.load(f)