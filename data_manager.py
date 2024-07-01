import json
import os

def initialize_json(file):
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump({"expenses": []}, f)
        print("Initialized expenses.json")

def load_data(file):
    with open(file, 'r') as f:
        return json.load(f)

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
