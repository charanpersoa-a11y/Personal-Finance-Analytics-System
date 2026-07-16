

import mypkg.services.auth as a
import mypkg.services.file_manager as f
import mypkg.services.dashboard as d

# first interface that user will se when the open
class interface():
    def __init__(self):
        print("====================================")
        print(" Personal Finance Analytics System")
        print("====================================")
        print("1.REGISTER ")
        print("2.LOGIN")
        print("3.EXIT")
        print("====================================")
        # options=[1,2,3]
        user_input=int(input("enter your choice :"))
        if user_input==1:
            name=input("enter your name..")
            age=int(input("enter your age .."))
            email=input("enter your email address...")
            password=input("enter your new password ...")
            a.Auth.Register(name=name,age=age,email=email,password=password)
            if a.Auth.Register:
                a.Auth.Login()



        elif user_input==2:
            users=f.load_users()
            print("your registration complete you can login with your id and password ..")
            a.Auth.Login()
            print("login successful you can proceed further .")
            print("if you want to see your dashboard please enter 1")
            enter=int(input("enter your choice number .."))
            if enter ==1:
                d.Dash.board()


        elif user_input==3:
            a.Auth.Exit()
        else:
            print("invalid input given please check your input again:.")


i=interface()




