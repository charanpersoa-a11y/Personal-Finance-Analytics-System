import json
from pathlib import Path
def load_users():
        users_path = Path("C:/coding/finance_project_/mypkg/data/users.json")
        try:
            with open(users_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

def save_users(users):
    users_path = Path("C:/coding/finance_project_/mypkg/data/users.json")
    with open(users_path, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

def add_user(user_id, name, age, gmail, password):
    users = load_users()
    users[user_id] = {
                    "name": name,
                    "age": age,
                    "email": gmail,
                    "password": password
                }
    save_users(users)
    # add_user(user_id, name, age, gmail, password)