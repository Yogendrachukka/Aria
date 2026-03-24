def update_relationship(memory, user_input):
    text = user_input.lower()

    if any(w in text for w in ["love", "miss", "baby"]):
        memory["affection_score"] += 2

    if any(w in text for w in ["ignore", "busy"]):
        memory["affection_score"] -= 3

    memory["affection_score"] = max(0, min(100, memory["affection_score"]))


def update_mood(memory, user_input):
    text = user_input.lower()

    if "who" in text:
        memory["last_mood"] = "jealous"
    elif "miss" in text:
        memory["last_mood"] = "clingy"