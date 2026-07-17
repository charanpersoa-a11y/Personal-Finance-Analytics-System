

from  mypkg.services.auth import Auth
import mypkg.services.file_manager as f
import mypkg.services.dashboard as d

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
            age=int(input("enter your age .."))
            email=input("enter your email address...")
            password=input("enter your new password ...")
            Auth.Register(name=name,age=age,email=email,password=password)
            print("registration complete you can login for more ")
            interface()



        elif user_input==2:
            users=f.load_users()
            # print("your registration complete you can login with your id and password ..")
            print("you have opted to login :")
            print("enter your id and password :")
            user_id=input("enter your id :-").strip()
            password=input("enter your password :-").strip()
            Auth.Login(user_id=user_id,user_password=password)
            print("login successful you can proceed further .")
            d.Dash.board()



        elif user_input==3:
            Auth.Exit()
        else:
            print("invalid input given please check your input again:.")


i=interface()




