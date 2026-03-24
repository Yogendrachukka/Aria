
import json
import os
import random


TELUGU_FILE = "aria/data/telugu_words.json"
LEARN_FILE = "aria/data/learned_slang.json"


def load_learned_slang():
    if os.path.exists(LEARN_FILE):
        with open(LEARN_FILE, "r") as f:
            return json.load(f)
    return {
        "romantic": [],
        "clingy": [],
        "attitude": [],
        "teasing": []
    }


def save_learned_slang(data):
    with open(LEARN_FILE, "w") as f:
        json.dump(data, f, indent=2)


def learn_slang(text, category="romantic"):
    data = load_learned_slang()

    for item in data[category]:
        if item["text"] == text:
            item["weight"] += 1
            save_learned_slang(data)
            print(f"📈 Increased weight: {text}")
            return

    # new slang
    data[category].append({
        "text": text,
        "weight": 1
    })

    save_learned_slang(data)
    print(f"🧠 Learned new slang: {text}")



def generate_telugu_slang(intent, telugu_dict):
    category = telugu_dict.get(intent, {})

    if not category:
        return ""

    key = random.choice(list(category.keys()))
    phrase = random.choice(category[key])

    return phrase

def load_telugu_words():
    if os.path.exists(TELUGU_FILE):
        with open(TELUGU_FILE, "r") as f:
            return json.load(f)
    return {}

def contains_telugu_word(text, telugu_dict):
    text = text.lower()

    for category in telugu_dict.values():
        for word in category.keys():
            if word in text:
                return True

    return False

def make_reply_short(text):
    return text[:120]

def is_telugu_style(text):
    telugu_keywords = ["ra", "enti", "nuvvu", "nenu", "inka", "chala"]
    text = text.lower()
    return any(word in text for word in telugu_keywords)



def weighted_choice(slang_list):
    if not slang_list:
        return None

    total = sum(item["weight"] for item in slang_list)
    r = random.uniform(0, total)

    upto = 0
    for item in slang_list:
        if upto + item["weight"] >= r:
            return item["text"]
        upto += item["weight"]

    return slang_list[-1]["text"]