# this is the place where all the budget things happen
import mypkg.services.file_manager as F
import mypkg.services.sessions as S
import mypkg.utlis.validation as V
class Budgets:
    def SetBudget(category,amount,limit):
        NewBudget=F.AddBudget(category=category,budget=amount,limit=limit)
        # print(f" your budget saved in our data and here it is {NewBudget}")

    def GetBudget(category):
        current_user=S.get_current_user()
        bud=F.LoadBudget()
        data=bud[current_user]
        if data  in bud:
            return data[category]



    def GetAll_Budgets():
        # users and transaction
        users=F.load_users()
        current_user=S.get_current_user()
        current_user_data=users[current_user]
        # budget
        All_Budget=F.LoadBudget()

        print("==============================================================")
        print(f"NAME: {current_user_data["name"]}")
        print(f"AGE: {current_user_data["age"]}")
        print(f"EMAIL ADDRESS : {current_user_data["email"]}")
        print("==============================================================")
        print("your transaction history ")
        trans=F.load_transaction()
        users_trans=trans[current_user]
        print(f"YOUR TRANSACTION HISTORY IS {users_trans}")
        print("==============================================================")
        print(f"your budget history ")
        if current_user in All_Budget:
            dashboard= All_Budget[current_user]
            print(f"your budget history is {dashboard}")
        else:
            print("currently you don't have and budget created yet ")
    def ShowSummary(self):
        print("==============================================================")
        bud=F.LoadBudget()
        current_user=S.get_current_user()
        user_bud=bud[current_user]
        for category ,entry in user_bud.items():
            print(f"CATEGORY :{category}")
            print(
                f"BUDGET:{entry["budget"]}|"
                f"LIMIT:{entry["limit"]}"
            )
        print("==============================================================")
    def SetBudget_Flow():
        category=input("enter your category:-")
        amount=V.ValidateAmount()
        limit=V.ValidateLimit()
        print("your budget is being processed ")
        Budgets.SetBudget(category=category,amount=amount,limit=limit)
        print("your budget is created ")
        print("="*25)

    def Menu(self):
        while True:
            print("1.SET BUDGET")
            print("2.VIEW ALL BUDGET ")
            print("3.EXIT")

            choice=int(input("enter your choice :-"))
            if choice==1:
                Budgets.SetBudget_Flow()
            elif choice==2:
                Budgets.GetAll_Budgets()
            elif choice==3:
                break
            else:
                print("invalid input.")
        









