
from  mypkg.services.auth import Auth
import mypkg.services.file_manager as f
import mypkg.services.dashboard as d
import mypkg.models.transactions as T
import mypkg.utlis.helper as H
import mypkg.utlis.validation as V
import time

# first interface that user will se when the open
class interface():
    def __init__(self):
        print("==========================================")
        print(" Personal Finance Analytics System")
        print("==========================================")
        print("1.REGISTER ")
        print("2.LOGIN")
        print("3.EXIT")
        print("====================================")
        # self.user_=Auth.Login.return_id()

        # options=[1,2,3]
        user_input=int(input("enter your choice :"))
        if user_input==1:
            name=input("enter your name..")
            # age=int(input("enter your age .."))
            email=input("enter your email address...")
            # password=input("enter your new password ...")
            age=V.ValidateAge()
            password=V.ValidatePassword()
            Auth.Register(name=name,age=age,email=email,password=password)
            print("registration complete you can login for more ")
            interface()



        elif user_input==2:
            print("LOGIN")
            user_id=input("enter your id :-").strip()
            password=input("enter your password :-").strip()
            Auth.Login(user_id=user_id,user_password=password)
            H.print_statements.login_main()
# helper file import here

            # time.sleep(3)
            d.Dash.board()
            # time.sleep(3)
            H.print_statements.options()
# import here

            # time.sleep(2)
            choice=int(input("enter your choice :-"))
            if choice==1:
                amount=int(input("enter your amount:-"))
                cat=["income ","expense"]
                for i , a in cat:
                    print(f"the options you have here is :-")
                    print(i,"    ",  a)
                print("choose your category from the above options .")
                print("anything other than income or expense won't be accepted ")
                category=input("enter the category of the transaction :-")
                date=time.strftime("%Y-%m-%d %H:%M:%S")
                type_=input("enter the type of transaction")
                T.add_transactions(amount=amount,category=category,date=date,type_=type_)
            elif choice==2:
                T.get_transaction_for_user()
            elif choice==3:
                # user=f.load_transaction()
                # print(user)
                print("copy the transaction id of the transaction you want to delete")
                t_id=int(input('enter the id '))
                transaction_id=(t_id)
                T.delete_transaction(transaction_id=transaction_id)
                print('your transaction id is successfully deleted ')
                print("==========================================")





        elif user_input==3:
            Auth.Exit()
        else:
            print("invalid input given please check your input again:.")


i=interface()
