import json
from pathlib import Path
import mypkg.services.sessions as S


# user part here 
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

# transaction part here 
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



# budget part here
def LoadBudget():
    bud=Path("C:/coding/finance_project_/mypkg/data/budgets.json")
    try:
        with open(bud,"r", encoding="utf-8") as B:
            return json.load(B)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
def SaveBudget(data):
    bud=Path("C:/coding/finance_project_/mypkg/data/budgets.json")
    with open(bud,"w", encoding="utf-8") as A:
        json.dump(data,A,indent=4)


def AddBudget( category, budget, limit,start_time):
    current_user = S.get_current_user()
    bud = LoadBudget()
    if current_user not in bud:
        bud[current_user] = {}
    bud[current_user][category] = {
        "limit": limit,
        "budget": budget,
        "start_time":start_time
    }
    SaveBudget(bud)
