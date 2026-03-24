from features.file_ops import create_folder, create_file


def handle_command(user_input, memory):

    text = user_input.lower()

    # 📁 create folder
    if text.startswith("create folder"):
        name = text.replace("create folder", "").strip()
        print(create_folder(name))
        return True

    # 📄 create file
    if text.startswith("create file"):
        name = text.replace("create file", "").strip()
        print(create_file(name))
        return True

    # existing commands
    if text == "/status":
        print(memory)
        return True

    if text == "/memory":
        print(memory.get("facts", []))
        return True

    if text == "/clear":
        import os
        if os.path.exists("aria/data/memory.json"):
            os.remove("aria/data/memory.json")
        print("Memory cleared")
        return True

    return False