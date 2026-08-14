import random as rd
import json
from pathlib import Path
import mypkg.models.user as u
from mypkg.services.file_manager import load_users , save_users
import mypkg.services.sessions as s

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
    def Login(user_id,user_password):
        users=load_users()

        # print("Entered password:", repr(password))
        # print("Stored password :", repr(users[user_id]["password"]))
        # print(users[user_id]["password"] == password)

        if user_id in users and users[user_id]["password"] == user_password:
            s.set_current_user(user_id=user_id)
            return user_id

        else:
            print("user id and password doesn't found please register :..")
            print("for register please enter 1 again ...")
            input_=int(input("enter you choice:..."))
            if input_==1:
                Auth.Register()


    def Exit():
        print("you have opted exit ")
        print("THANK YOU")
        s.clear_current_user()

# U=UserInput()
