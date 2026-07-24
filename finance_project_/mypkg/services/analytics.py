# the analysis part of this project will be here
# what are the initial things we are working here is first the period i budget we a gonna set a period of a budget or the user will tel us the period and 
# we will calculate the remaining time or the end time .
# the first whenever a user create a new transaction with a category the amount will be deducted from his budget .
# TRANSACTION IN CATEGORY FOOD AMOUNT 500
# GO TO BUDGET AND GET THE USERS INFO THEN GO TO THE CATEGORY FOOD THEN DEDUCT THE AMOUNT FROM THE BUDGET AND GIVE HIM A NOTIFICATION

import mypkg.services.sessions as S
import mypkg.models.budget as B
import mypkg.models.transaction as T
import mypkg.services.file_manager as F

# this will be calculated over a category
def IncomeVsExpense():
    category=input("enter your category or choose one :-").strip().upper()
    Get_Total_categoryTransactions(category=category)
    print('')



    # data 2 is budget
    # data2=TData2[current_user]
    
def Get_Total_categoryTransactions(category):
    current_user=S.get_current_user()
    TData1=F.load_transaction()
    TData2=F.LoadBudget()
        # data1 is transactions
    data1=TData1[current_user]
    total=0
    for transaction_id  in data1:
        for entry in data1[transaction_id].items():
            if entry.get("category","")==category:
                amount= entry.get("amount",0)
                total+=amount
                return total
            else:
                return None



