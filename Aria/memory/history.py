import os
import json

HISTORY_FILE_PATH = "aria/data/chat_history.json"

def load_history():
    # 1. Get the directory path and create it if it doesn't exist
    directory = os.path.dirname(HISTORY_FILE_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    
    # 2. Check if the file exists before trying to read it
    if not os.path.exists(HISTORY_FILE_PATH):
        # Create an initial empty history file
        with open(HISTORY_FILE_PATH, "w") as file:
            json.dump([], file)
        return []

    # 3. Read the file safely
    try:
        with open(HISTORY_FILE_PATH, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # If the file is empty or corrupted, return an empty history
        return []

def log_message(history, role, content):
    # Append to the history list
    history.append({"role": role, "content": content})
    
    # Save the updated history back to the file
    with open(HISTORY_FILE_PATH, "w") as file:
        json.dump(history, file, indent=4)
