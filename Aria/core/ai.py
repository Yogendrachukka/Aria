import time
import random
from config import client, MODEL_NAME
from utils.helpers import generate_telugu_slang, load_telugu_words, weighted_choice
from core.personality import get_system_prompt
from utils.helpers import load_learned_slang
import random

learned = load_learned_slang()

def get_ai_response(messages, memory):

    clean_messages = [
        {"role": m["role"], "content": m["content"]}
        for m in messages[-20:]
    ]

    print("\nAria is typing...", flush=True)
    time.sleep(1)

    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": get_system_prompt(memory, clean_messages[-1]["content"])},
            *clean_messages
        ],
        temperature=0.9,
        max_tokens=200
    )

    reply = res.choices[0].message.content
        # 🌐 Telugu slang enhancement
    telugu_dict = load_telugu_words()

    if memory.get("language_mode") == "telugu":
        mood = memory.get("last_mood", "happy")

        if mood == "clingy":
            intent = "clingy"
        elif mood == "jealous":
            intent = "attitude"
        else:
            intent = "romantic"

            # combine default + learned slang
            base_slang = generate_telugu_slang(intent, telugu_dict)
            learned_slang = learned.get(intent, [])
                
            if learned_slang:
                slang = weighted_choice(learned_slang)
            else:
                slang = generate_telugu_slang(intent, telugu_dict)

            if slang:
                reply = f"{slang}… {reply}"
                        
    return reply