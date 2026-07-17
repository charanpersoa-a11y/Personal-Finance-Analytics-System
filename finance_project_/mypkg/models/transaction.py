# this is the most important thing right now
# here all the transactions of the user will happen
# main structure of this transaction is
# Transaction
# ├── transaction_id
# ├── amount
# ├── date
# ├── description
# this is the structure of the transaction\
import mypkg.services.sessions as S
import mypkg.services.file_manager as f
import time as t
class Transaction():
    def __init__(self,amount,t_type,date,transaction_id):
        self.amount=amount
        self.t_type=t_type
        self.date=date
        self.transaction_id=transaction_id

    def to_trans(self):
        return {
            "transaction_id":self.transaction_id,
            "amount":self.amount,
            "type":self.t_type,
            "date":self.date
        }






