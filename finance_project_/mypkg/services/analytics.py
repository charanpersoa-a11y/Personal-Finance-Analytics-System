# the analysis part of this project will be here
# what are the initial things we are working here is first the period i budget we a gonna set a period of a budget or the user will tel us the period and 
# we will calculate the remaining time or the end time .
# the first whenever a user create a new transaction with a category the amount will be deducted from his budget .
# TRANSACTION IN CATEGORY FOOD AMOUNT 500
# GO TO BUDGET AND GET THE USERS INFO THEN GO TO THE CATEGORY FOOD THEN DEDUCT THE AMOUNT FROM THE BUDGET AND GIVE HIM A NOTIFICATION
# i am thinking of calculating the income vs expense in transaction first then move to budget


import mypkg.services.sessions as S
import mypkg.models.budget as B
import mypkg.models.transaction as T
import mypkg.services.file_manager as F

# this will be calculated over a category
def AnalysisMenu():
    print("==========================================")
    print("COMPLETE ANALYSIS OF YOUR BUDGET AND TRANSACTION")
    category=input("enter your category or choose one :-").strip().upper()
    TotalIncome=Get_Total_categoryTransactionsI(category=category)
    TotalExpense=Get_Total_CAtegory_transactionE(category=category)
    TotalBudget=Get_Total_Category_Budget(category=category)
    RemainingBudget=TotalBudget-TotalExpense
    print(f"your total budget for this category {category} is {TotalBudget}")
    print(f"your total income in this time period is {TotalIncome}")
    print((f"your total expense in this time period is {TotalExpense}"))
    print(f"your remaining budget for {category} is {RemainingBudget}")
    print("==========================================")


    # data 2 is budget
    # data2=TData2[current_user]
# total of income in transaction will be here
def Get_Total_categoryTransactionsI(category):
    current_user=S.get_current_user()
    TData1=F.load_transaction()

        # data1 is transactions
    data1=TData1[current_user]
    total=0
    for transaction_id ,entry in data1.items():
        if entry.get("type_")=="income" and entry.get("category","")==category:
            amount= entry.get("amount",0)
            total+=amount

    return total if total>0 else None

# total of expense in transaction will be here
def Get_Total_CAtegory_transactionE(category):
    current_user=S.get_current_user()
    TData1=F.load_transaction()

        # data1 is transactions
    data1=TData1[current_user]
    total=0
    for transaction_id, entry in data1.items():
        if entry.get("type_") == "expense" and entry.get("category", "") == category:
            total += entry.get("amount", 0)

    return total if total > 0 else None


def Get_Total_Category_Budget(category):
    TData2=F.LoadBudget()
    current_user=S.get_current_user()
    data2=TData2[current_user]
    total=0

    for category, entry in data2.items():
        if category==category:
            amount=entry.get("budget","")
            total=amount
            return total

