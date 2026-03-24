import json
import os

MEMORY_FILE = "aria/data/memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    return {
        "facts": [],
        "name": "babe",
        "affection_score": 50,
        "relationship_level": 1,
        "personality_traits": {
            "clinginess": 0.5,
            "jealousy": 0.3,
            "playfulness": 0.7
        },
        "last_mood": "happy"
    }

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)