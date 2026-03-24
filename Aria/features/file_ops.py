import os

BASE_DIR = "Aria"  # root folder


def create_folder(folder_name):
    path = os.path.join(BASE_DIR, folder_name)

    if not os.path.exists(path):
        os.makedirs(path)
        return f"📁 Created folder: {folder_name}"
    else:
        return f"⚠️ Folder already exists: {folder_name}"


def create_file(file_path):
    path = os.path.join(BASE_DIR, file_path)

    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("")
        return f"📄 Created file: {file_path}"
    else:
        return f"⚠️ File already exists: {file_path}"