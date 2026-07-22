
from  mypkg.services.auth import Auth
import mypkg.services.file_manager as f
import mypkg.services.dashboard as d
import mypkg.models.transactions as T
import mypkg.utlis.helper as H
import mypkg.utlis.validation as V
import mypkg.models.budget as B
import time
import mypkg.services.sessions as S
class Dash():

    def Menu():
        users_id=S.get_current_user()
        users=f.load_users()
        # print("user summary")
        summary=T.show_summary(user_id=users_id)
        # transaction menu will be showed here
        T.Menu()
        # the budget menu will be showed here
        b=B.Budgets()
        b.Menu()

    
       