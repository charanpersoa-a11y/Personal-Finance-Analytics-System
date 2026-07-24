
from  mypkg.services.auth import Auth
import mypkg.services.file_manager as f
import mypkg.services.dashboard as d
import mypkg.models.transactions as T
import mypkg.utlis.helper as H
import mypkg.utlis.validation as V
import mypkg.models.budget as B
import time
import mypkg.services.analytics as A
import mypkg.services.sessions as S

class Dash():

    def Menu():
        users_id=S.get_current_user()
        # users=f.load_users()
        # print("user summary")
        # this is the summary of the transaction 
        summary=T.show_summary(user_id=users_id)
    
        # transaction menu will be showed here
        T.Menu()
        
        # the budget summary will be shown here
        a=B.Budgets()
        a.ShowSummary()
        # the budget menu will be showed here
        b=B.Budgets()
        b.Menu()
        # analysis menu
        A.AnalysisMenu()
        t=H.DateTime_Calculations()
        t.Get_period()


    
       