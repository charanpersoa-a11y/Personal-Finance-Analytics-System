# this helper file i will use it for the showing things like i use a lot of print statements in this projects and i want to organize them in one place 
class print_statements():
    def login_main():
        print("login successful you can proceed further .")

    def options():
        print("1. To add a new transaction")
        print("2. Get transaction ")
        print("3. to delete a specific transaction..")


import time as T
import datetime as DT
import mypkg.services.file_manager as F
import mypkg.services.sessions as S
class DateTime_Calculations():
    def Get_period(self):
        current_user=S.get_current_user()
        budget=F.LoadBudget()
        user_budget=budget[current_user]

        # start_date=user_budget[]
        for category , entry in user_budget.items():
            # print(category)
            start_date=entry["start_time"]
            start_date=DT.date.fromisoformat(start_date)
            period=31
            end_date=start_date + DT.timedelta(period)
            print(f"the last date for {category} is {end_date}")

