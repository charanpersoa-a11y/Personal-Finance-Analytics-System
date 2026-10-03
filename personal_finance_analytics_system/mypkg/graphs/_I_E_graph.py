import mypkg.analysis.income_analysis as I
import mypkg.analysis.expense_analysis as E
import mypkg.analysis.savings_analysis as S
import matplotlib.pyplot as plt



def BarchartIE(ax):
    data = {"Income": I.TotalIncome(), "Expense": E.TotalExpense(), "Savings": S.Savings()}
    bars = ax.bar(data.keys(), data.values(), color=["green", "red", "gold"])
    ax.set_title("Income vs Expense vs Savings")
    ax.set_ylabel("Amount")
    ax.grid(axis="y")
    ax.bar_label(bars)


def PieChartExpenseByCategory(ax):
    data = E.ExpenseByCategory()
    ax.pie(data.values, labels=data.index, autopct="%1.1f%%")
    ax.set_title("Expense by Category")


# def DonutExpenseByCategory(ax):
#     data = E.ExpenseByCategory()
#     ax.pie(data.values, labels=data.index, autopct="%1.1f%%", wedgeprops={"width": 0.4})
#     ax.set_title("Expense Breakdown")


def ChartsDisplay():
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    BarchartIE(ax[0])
    PieChartExpenseByCategory(ax[1])
    # DonutExpenseByCategory(ax=ax[1,0])
    # ax[0,1], ax[1,0], ax[1,1] — other charts go here later
    plt.tight_layout()
    plt.show()