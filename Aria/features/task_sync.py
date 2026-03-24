import json
import os
import uuid

TASK_FILE = "aria/data/tasks.json"


# ─────────────────────────────────────────────
# 📁 LOAD TASKS (safe)
# ─────────────────────────────────────────────
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []

    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except:
        return []


# ─────────────────────────────────────────────
# 💾 SAVE TASKS
# ─────────────────────────────────────────────
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


# ─────────────────────────────────────────────
# ➕ ADD TASK
# ─────────────────────────────────────────────
def add_task(command):
    tasks = load_tasks()

    new_task = {
        "id": str(uuid.uuid4()),   # ✅ unique ID
        "cmd": command,
        "status": "pending"        # ✅ better than done flag
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f"📡 Task added: {command}")


# ─────────────────────────────────────────────
# 📡 GET PENDING TASKS
# ─────────────────────────────────────────────
def get_pending_tasks():
    tasks = load_tasks()
    return [t for t in tasks if t.get("status") == "pending"]


# ─────────────────────────────────────────────
# ✅ MARK TASK COMPLETE
# ─────────────────────────────────────────────
def mark_done(task_id):
    tasks = load_tasks()

    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "done"

    save_tasks(tasks)