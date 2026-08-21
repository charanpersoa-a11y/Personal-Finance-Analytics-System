import mypkg.analysis.data_processor as D
import mypkg.analysis.expense_analysis as E
import mypkg.analysis.income_analysis as I

def Savings():
    return I.TotalIncome() - E.TotalExpense()

def SavingsRate():
    income = I.TotalIncome()
    return (Savings() / income) * 100 if income else 0

def PositiveCashFlow():
    return I.TotalIncome() > E.TotalExpense()

def NetReport():
    print("====================================================")
    print(f"total savings: {Savings()}")
    print(f"savings rate: {SavingsRate():.2f}%")
    print(f"cash flow status: {'positive' if PositiveCashFlow() else 'negative'}")
    print("====================================================")