# this is the place where all the budget things happen
import mypkg.services.file_manager as F
import mypkg.services.sessions as S
class Budgets:
    def SetBudget(self,category,amount,limit):
        self.category=category
        self.amount=amount
        self.limit=limit
        NewBudget=F.AddBudget(category=category,amount=amount,limit=limit)
        print(f" your budget saved in our data and here it is {NewBudget}")

    def GetBudget(category):
        current_user=S.get_current_user()
        bud=F.LoadBudget()
        data=bud[current_user]
        if data  in bud:
            return data[category]



    def GetAll_Budgets():
        current_user=S.get_current_user()
        All_Budget=F.LoadBudget()
        if current_user in All_Budget:
            return All_Budget[current_user]






