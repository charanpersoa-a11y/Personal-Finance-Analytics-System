# here all the transactions happens
import mypkg.services.sessions as S
import random as rd
import mypkg.services.file_manager as F
import mypkg.models.transaction as T
import pathlib as P
import json



def add_transactions(amount,category,date,type_):
    current_user=S.get_current_user()
    digits = rd.sample(range(5), 5)
    transaction_id = "".join(map(str, digits))
    transaction=F.load_transaction()
    if current_user not in transaction:
        transaction[current_user]={}
    transaction[current_user][transaction_id] = {
        "amount": amount,
        "category": category,
        "date": date,
        "type": type_
    }
    # new_transaction=T.Transaction(amount=amount,t_type=None,date=None,transaction_id=transaction_id)
    F.save_transaction(transaction)

def get_transaction_for_user():
    current_user=S.get_current_user()
    data=F.load_transaction()
    try:

        trans=data[current_user]
        if trans in data:
            return trans
        else:
            print("currently you don't have any registrations yet")
    except Exception as e:
        print(f"error occurs as {e}")

    print(f"the transactions of the user is ")
    print(trans)

def delete_transaction(transaction_id):
    # trans = F.load_transaction()
    current_user = S.get_current_user()

    data = P.Path("C:/coding/finance_project_/mypkg/data/transactions.json")

    users=F.load_transaction()

    print(users[current_user])

    if current_user in users and transaction_id in users[current_user]:
        del users[current_user][transaction_id]

    with open(data, "w", encoding="utf-8") as u:
        json.dump(users, u, indent=4)


def edit_transaction(transaction_id):
    print("NOTE: TRANSACTION ID CANNOT BE EDITED OR CHANGED .")
    print("the things you can edit now are amount category and type of transaction ")
    print("your transaction data is")
    current_user=S.get_current_user()
    data=P.Path("C:/coding/finance_project_/mypkg/data/transactions.json")
    with open(data,"r", encoding="utf-8") as f:
        users=json.load(f)
    print(users[current_user])

    print("=================================")
    print("things you can change.")
    change=["amount" , "category","type_"]
    for i , a in enumerate(change):
        print(i,"     ", a)
    print("choose which one to change")


def show_summary(user_id):
    transactions=F.load_transaction()
    users=F.load_users()
    print("TRANSACTION SUMMARY.")
    name=users[user_id]["name"]
    email=users[user_id]["email"]
    print(f"NAME: {name}")
    print(f"EMAIL: {email}")
    for user_id, entries in transactions.items():
        print(f"User: {user_id}")
        for entry_id, entry in entries.items():
            print(f"  ID: {entry_id} | amount: {entry['amount']} | category: {entry['category']} | date: {entry['date']} | type: {entry['type']}")

    

