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

def load_transaction():
    user_path=Path(r"C:/coding/finance_project_/mypkg/data/transactions.json")
    try:
        with open(user_path,"r",encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_transaction(transact):
    user_path=Path(r"C:/coding/finance_project_/mypkg/data/transactions.json")
    with open(user_path,"w",encoding="utf-8") as f:
        json.dump(transact,f,indent=4)

def add_transaction(user_id,amount,type,transaction_id):
    transaction=load_transaction()
    transaction[user_id]={"transaction_id":transaction_id,
                          "amount":amount,
                          "type":type
                          }
    save_transaction(transaction)