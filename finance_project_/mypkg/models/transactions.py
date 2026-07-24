# here all the transactions happens
import mypkg.services.sessions as S
import random as rd
import mypkg.services.file_manager as F
import mypkg.models.transaction as T
import pathlib as P
import json
import time

# i am changing or swapping category with transaction id
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
        "type_":type_
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


def show_summary(user_id):
    transactions = F.load_transaction()
    users = F.load_users()
    trans = transactions[user_id]
    print("TRANSACTION SUMMARY.")
    name = users[user_id]["name"]
    email = users[user_id]["email"]
    print(f"NAME: {name}")
    print(f"EMAIL: {email}")
    if user_id in transactions:
        for transaction_id, entry in trans.items():
            print("-" * 60)
            print(f"TRANSACTION ID: {transaction_id}")
            print(
                f"Amount: {entry['amount']} | "
                f"Category: {entry['category']} | "
                f"Date: {entry['date']} | "
                f"type_:{entry['type_']} |"
            )

        print()
    else:
        print("no transactions yet")

def ADD_TRANSACTION_FLOW():
    amount=int(input("enter the amount:-"))
    cat=["FOOD","GROCERY",'RENT','OTHER EXPENSE']
    for i , a in enumerate(cat):
        print(i,"    ",a )
    category=input("select  your category :-").strip().upper()
    date = time.strftime("%Y-%m-%d")
    ty=["INCOME","EXPENSE"]
    print("NOTE type should be of only types they are ")
    for i , t in enumerate(ty):
        print(i,"   ", t)
    print("please select one of these and move")
    type_=None
    choice=int(input("enter your choice:-"))
    if choice==1:
        type_="INCOME"
    elif choice==2:
        type_="EXPENSE"
    else:
        print("invalid input")
    add_transactions(amount=amount,category=category,date=date,type_=type_)

def Delete_transaction_flow():
    transaction_id=int(input("enter your transaction id"))
    print('copy the transaction id you want to delete form the above summary')
    delete_transaction(transaction_id=transaction_id)





def Menu():
    while True:
        print("1.ADD TRANSACTION")
        print('2. VIEW TRANSACTION')
        print('3.DELETE TRANSACTION')
        print("4.EXIT")

        choice=int(input("enter your choice:-"))
        if choice==1:
            ADD_TRANSACTION_FLOW()
        elif choice==2:
            get_transaction_for_user()

        elif choice==3:
            Delete_transaction_flow()
        elif choice==4:
            break
        else:
            print("invalid input")

