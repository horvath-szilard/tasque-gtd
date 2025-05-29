# test_seed_data.py

import requests

BASE_URL = "http://127.0.0.1:8000"

# -------------------
# Create Projects
# -------------------
projects = [
    {"name": "Webshop redesign", "description": "Frontend + backend refactor"},
    {"name": "Mobile app", "description": "New feature planning"}
]

project_ids = []
for project in projects:
    res = requests.post(f"{BASE_URL}/projects/", json=project)
    try:
        data = res.json()
        if res.status_code == 200:
            print("Project:", res.status_code, data)
            project_ids.append(data["id"])
        else:
            print("Project (error):", res.status_code, data)
    except Exception as e:
        print("Project (invalid response):", res.status_code, res.text)

# -------------------
# Create Contexts (only if they don't exist)
# -------------------
contexts = ["Office", "Home", "Errands"]
context_ids = []

for name in contexts:
    res = requests.post(f"{BASE_URL}/contexts/", json={"name": name})
    try:
        data = res.json()
        if res.status_code == 200:
            print("Context:", res.status_code, data)
            context_ids.append(data["id"])
        elif res.status_code == 400 and "already exists" in str(data):
            print("Context already exists:", name)
            # Try to find the existing ID via /contexts/
            all_contexts = requests.get(f"{BASE_URL}/contexts/").json()
            existing = next((ctx for ctx in all_contexts if ctx["name"] == name), None)
            if existing:
                context_ids.append(existing["id"])
        else:
            print("Context (error):", res.status_code, data)
    except Exception as e:
        print("Context (invalid response):", res.status_code, res.text)

# -------------------
# Create Tasks
# -------------------
if len(context_ids) < 2 or len(project_ids) < 1:
    print("⚠️ Not enough context or project IDs. Cannot continue creating tasks.")
else:
    tasks = [
        {"title": "Buy printer ink", "type": "next_action", "context_id": context_ids[2]},
        {"title": "Call Alex", "type": "waiting", "context_id": context_ids[0]},
        {"title": "Research analytics tool", "type": "someday"},
        {"title": "Migrate database", "type": "next_action", "project_id": project_ids[0]},
        {"title": "Write release notes", "type": "inbox"}
    ]

    for task in tasks:
        res = requests.post(f"{BASE_URL}/tasks/", json=task)
        try:
            data = res.json()
            if res.status_code == 200:
                print("Task:", res.status_code, data)
            else:
                print("Task (error):", res.status_code, data)
        except Exception as e:
            print("Task (invalid response):", res.status_code, res.text)