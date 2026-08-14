import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mypkg.services.file_manager as F
import mypkg.services.analytics as A
import mypkg.services.sessions as S


def Chart():
    # chart for a individual category
    # category =input("enter your category:-")
    current_user=S.get_current_user()
    income=A.Get_Total_categoryTransactionsI()
    expense=A.Get_Total_CAtegory_transactionE()
    budget_file=F.LoadBudget()
    budget_user=budget_file[current_user]
    list_category=[category for category in budget_user]
    list_amount=[]
    for category in budget_user:
        list_amount.append(budget_user[category]["budget"])
    color=["blue","green","pink","gold"]

    plt.bar(list_category,list_amount,color=color)
    Label=["INCOME" , 'EXPENSE']
    # plt.pie(income,expense,labels=Label)

    plt.show()

import matplotlib.pyplot as plt
# expense distribution graph basically pie chart 
def Pie_chart():
    color=['b','r','g','c','m','y','k','w']
    category,amount =A.expense_pie_data()
    plt.pie(amount, labels=category , colors=color, autopct="%1.1f%%")
    plt.title("expense distribution chart ")
    plt.axis("equal")
    plt.show()


def ShowCharts():
    fig,ax=plt.subplots(2,2,figsize=(10,8))
    ax[0,0]=Chart()
    ax[0,1]=Pie_chart()