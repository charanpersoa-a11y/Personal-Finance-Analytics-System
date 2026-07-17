# here all the transactions happens
import mypkg.services.sessions as S
import random as rd
import mypkg.services.file_manager as F
import mypkg.models.transaction as T




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
    trans=data[current_user]
    print(f"the transactions of the user is ")
    print(trans)


