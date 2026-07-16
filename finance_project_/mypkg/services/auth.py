import random as rd
import json
from pathlib import Path
import models.user as u
from file_manager import load_users , save_users

class Auth():
        # register block
    def Register(name,age,email,password):
        digits = rd.sample(range(10), 10)
        user_id = "".join(map(str, digits))
        new_user = u.User( name, age, email,password=password)
        users = load_users()
        users[user_id] = new_user.to_dict()
        save_users(users)

        print("Your generated ID is:", user_id)
        print(f"please remember this id for login purposes .. {user_id}")
        print(f"your password is {password} note down this for login processes ..")
        print("register process complete you can proceed further .")
        print("YOUR DATA IS SAVED IN OUR DATABASE :......")
        print("you can log in with your used id and password ....")
        print("-----------------------------------")


                # load_users()
    # login block
    def Login():
        print("you have opted to login :")
        print("enter your id and password :")
        path="C:/coding/finance_project_/mypkg/data/users.json"
        with open(path,"r") as f:
            users=json.load(f)
            print(users)

        id=input("enter your id :-").strip()
        password=input("enter your password :-").strip()
        print("Entered password:", repr(password))
        print("Stored password :", repr(users[id]["password"]))
        print(users[id]["password"] == password)

        if id in users:
            if users[id]["password"] == password:
                return id

                # dashboard of the logged in user.

            else:
                print("Invalid Password")
                print("PLEASE CHECK YOUR PASSWORD AND TRY AGAIN>>.")

        else:
            print("user id and password doesn't found please register :..")
            print("for register please enter 1 again ...")
            input_=int(input("enter you choice:..."))
            if input_==1:
                Auth.Register()

    def Exit():
        print("you have opted exit ")
        print("THANK YOU")

# U=UserInput()
