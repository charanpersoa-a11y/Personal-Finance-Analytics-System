import random as rd
import json 
from pathlib import Path
class UserInput():
    def __init__(self):
        id_password={}

        # register block
        def Register():

            print("you opted to register:")
            print("please follow the below instructions:")
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            gmail = input("Enter your email id: ")

            digits = rd.sample(range(10), 10)
            user_id = "".join(map(str, digits))

            password = input("Set a new strong password: ")

            users = {}

            users[user_id] = {
                        "name": name,
                        "age": age,
                        "email": gmail,
                        "password": password
}
            # for users[user_id]["name"] in users:
            #     if name in users[user_id]["name"]:
            #         print("name already exists please enter a different version of your name ..")
            #     else:
            #         pass
            # users_file=Path("users.json")
            # def load_users():
            #     if not users_file.exists():
            #         return []
            #     with users_file.open("r", encoding="utf-8") as f:
            #         return json.load(f)

            # path="C:/coding/finance_project_/data/users.json"
            # with open(path, "a", encoding="utf-8") as f:
            #     json.dump(users,f)
            #     print("\n")


            users_path = "users.json"

            def load_users():
                try:
                    with open(users_path, "r", encoding="utf-8") as f:
                        return json.load(f)
                except (FileNotFoundError, json.JSONDecodeError):
                    return {}

            def save_users(users):
                with open(users_path, "w", encoding="utf-8") as f:
                    json.dump(users, f, indent=4)

            def add_user(user_id, name, age, gmail, password):
                users = load_users()
                users[user_id] = {
                    "name": name,
                    "age": age,
                    "email": gmail,
                    "password": password
                }
                save_users(users)


            print("Your generated ID is:", user_id)
            print(f"please remember this id for login purposes .. {user_id}")
            print("-----------------------------------")
            print("register process complete you can proceed further .")
            print("YOUR DATA IS SAVED IN OUR DATABASE :......")

            # load_users()
# login block
        def Login():
            print("you have opted to login :")
            print("enter your id and password :")
            path="C:/coding/finance_project_/data/users.json"
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
                    print("Login Successful")
                else:
                    print("Invalid Password")
                    print("PLEASE CHECK YOUR PASSWORD AND TRY AGAIN>>.")

            else:
                print("user id and password doesn't found please register :..")
                print("for register please enter 1 again ...")
                input_=int(input("enter you choice:..."))
                if input_==1:
                    Register()


        def Exit():
            print("you have opted exit ")
            print("THANK YOU")
        print(id_password)

        user_input=int(input("enter your choice :"))
        if user_input==1:
            Register()
        elif user_input==2:
            Login()
        elif user_input==3:
            Exit()
        else:
            print("invalid input given please check your input again:.")
U=UserInput()
