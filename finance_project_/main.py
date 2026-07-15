

from mypkg.services import auth

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
            auth.Auth.Register(name=name,age=age,email=email,password=password)



        elif user_input==2:
            auth.Login()
        elif user_input==3:
            auth.Exit()
        else:
            print("invalid input given please check your input again:.")


i=interface()




