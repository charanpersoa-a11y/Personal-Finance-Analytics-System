import random as rd
import json as js
class UserInput():
    def __init__(self):
        id_password={}
        user_input=int(input("enter your choice :"))
        if user_input==1:
            print("you opted to register:")
            print("please follow the below instructions:")
            name=input("enter your name :-")
            age=input("enter your age :-")
            gmail=input("enter your email id :-")
            id_password = {}
            digits = rd.sample(range(0, 10), 10)
            user_id = int("".join(map(str, digits)))
            password = input("set a new strong password :- ")
            for i in range(len(id_password)+1):
                id_password[user_id]=password
            
            with open(r"C:\coding\finance_project_\data\users.json") as f:
                js.dump(id_password,f)





            print("Your generated ID is:", user_id)
            print(id_password)
            print("-----------------------------------")
            print("register process complete you can proceed further .")

        elif user_input==2:
            print("you have opted to login :")
            print("enter your id and password :")
            id=int(input("enter your id :-"))
            password=input("enter your password :-")
                        # have to ensure the data but that things will be done next day 
            print("login successful you can proceed ..")
        elif user_input==3:
            print("you have opted exit ")
            print("THANK YOU")
U=UserInput()