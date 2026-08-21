import mypkg.analysis.data_processor as D
import pandas as pd
import numpy as np


def TotalIncome():
    rows = D.IncomeRows()
    return rows["amount"].sum() if not rows.empty else 0

def IncomeCount():
    return D.IncomeRows().shape[0]

def AverageIncome():
    rows = D.IncomeRows()
    return rows["amount"].mean() if not rows.empty else 0

def HighestIncomeTransaction():
    rows = D.IncomeRows()
    if rows.empty:
        return None
    return rows.loc[rows["amount"].idxmax()]

def IncomeBySource():
    rows = D.IncomeRows()
    return rows.groupby("category")["amount"].sum()

def MonthlyIncome():
    rows = D.IncomeRows()
    return rows.groupby(rows["date_"].dt.to_period("M"))["amount"].sum()

def IncomeReport():
    print("====================================================")
    print("your income in each category")
    print(IncomeBySource())
    print(f"your total income is {TotalIncome()}")
    print(f"highest income transaction is\n{HighestIncomeTransaction()}")
    print(f"monthly income breakdown:\n{MonthlyIncome()}")
    print("====================================================")