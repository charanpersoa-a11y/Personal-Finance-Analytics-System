import mypkg.analysis.data_processor as D
import pandas as pd
import numpy as np


def TotalExpense():
    rows = D.ExpenseRows()
    return rows["amount"].sum() if not rows.empty else 0

def ExpenseCount():
    return D.ExpenseRows().shape[0]

def AverageExpense():
    rows = D.ExpenseRows()
    return rows["amount"].mean() if not rows.empty else 0

def HighestExpenseTransaction():
    rows = D.ExpenseRows()
    if rows.empty:
        return None
    return rows.loc[rows["amount"].idxmax()]

def ExpenseByCategory():
    rows = D.ExpenseRows()
    return rows.groupby("category")["amount"].sum()

def MonthlyExpense():
    rows = D.ExpenseRows()
    return rows.groupby(rows["date_"].dt.to_period("M"))["amount"].sum()

def ExpenseReport():
    print("====================================================")
    print("your expenses in each category")
    print(ExpenseByCategory())
    print(f"your total expense is {TotalExpense()}")
    print(f"highest expense transaction is\n{HighestExpenseTransaction()}")
    print(f"monthly expense breakdown:\n{MonthlyExpense()}")
    print("====================================================")