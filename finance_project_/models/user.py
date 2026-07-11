import random as rd
import json 
import os
class UserInput():
    def __init__(self):
        id_password={}
        user_input=int(input("enter your choice :"))
        if user_input==1:
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

            # else:
            #     print("USER ALREADY EXIST PLEASE SELECT LOGIN:..")
            path="C:/coding/finance_project_/data/users.json"
            with open(path, "w", encoding="utf-8") as f:
                json.dump(users,f)


            # with open("users.json", "w", encoding="utf-8") as f:
            #         js.dump(id_password, f, ensure_ascii=False, indent=4)


            print("Your generated ID is:", user_id)
            print("-----------------------------------")
            print("register process complete you can proceed further .")
            print("YOUR DATA IS SAVED IN OUR DATABASE :......")

        elif user_input==2:
            print("you have opted to login :")
            print("enter your id and password :")
            path="C:/coding/finance_project_/data/users.json"
            with open(path,"r") as f:
                users=json.load(f)
                print(users)

            
            id=input("enter your id :-").strip()
            password=input("enter your password :-").strip()
            # print("Entered password:", repr(password))
            # print("Stored password :", repr(users[id]["password"]))
            # print(users[id]["password"] == password)

            if id in users:
                if users[id]["password"] == password:
                    print("Login Successful")
                else:
                    print("Invalid Password")
                    print("PLEASE CHECK YOUR PASSWORD AND TRY AGAIN>>.")
            
            else:
                print("user id and password doesn't found please register :..")
                from main_.main import interface

                
                
                        # have to ensure the data but that things will be done next day
            # for keys in users:
            #     if id in keys:
            #         print("user available ...")
            #         print("enter your password for login ..")
            #     else:
            #         print("login information not found please register ")
            #         
            # print("login successful you can proceed ..")
        elif user_input==3:
            print("you have opted exit ")
            print("THANK YOU")
        print(id_password)
U=UserInput()
