from memory.memory import load_memory, save_memory
from memory.history import load_history, log_message
from core.ai import get_ai_response
from core.evolution import update_relationship, update_mood
from features.commands import handle_command
from features.task_sync import get_pending_tasks, mark_done
import time
from utils.helpers import load_telugu_words, contains_telugu_word
from utils.helpers import learn_slang, is_telugu_style


telugu_dict = load_telugu_words()
memory = load_memory()
history = load_history()

name = memory["name"]

print(f"\n💕 Aria: hey {name}… I missed you 🥺❤️\n")

while True:
    try:
        # 🔄 1. CHECK REMOTE TASKS FIRST
        tasks = get_pending_tasks()

        for task in tasks:
            print(f"\n📡 Remote Task: {task['cmd']}")

            handled = handle_command(task["cmd"], memory)

            if handled:
                mark_done(task["id"])

        # 👤 2. USER INPUT
        user_input = input(f"{name}: ").strip()
        

        if user_input.lower() in ["quit", "exit", "see you later"]:
            print("Aria: don't go 🥺")
            break
        
        elif is_telugu_style(user_input):
            learn_slang(user_input, "romantic")

        elif contains_telugu_word(user_input, telugu_dict):
           memory["language_mode"] = "telugu"

        # 🧠 3. COMMANDS (local)
        if handle_command(user_input, memory):
            continue

        # 💾 4. SAVE USER MESSAGE
        log_message(history, "user", user_input)

        # 💕 5. EVOLUTION SYSTEM
        update_relationship(memory, user_input)
        update_mood(memory, user_input)
        save_memory(memory)

        # 🤖 6. AI RESPONSE
        reply = get_ai_response(history, memory)
        print(f"\nAria: {reply}\n")

        # 💾 7. SAVE AI MESSAGE
        log_message(history, "assistant", reply)

    except KeyboardInterrupt:
        print("\nAria: hey… come back soon 😤❤️\n")
        break

    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        break