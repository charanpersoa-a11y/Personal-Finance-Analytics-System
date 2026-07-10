# project for my resume
# i will include file handling exception handling oops concepts and many libraries here in this project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os as o
import random as rd
import time as t

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
        # for val in options:
        if user_input==1:
            print("you opted to register:")
            print("please follow the below instructions:")
        elif user_input==2:
            print("you have opted to login :")
            print("enter your id and password :")
        elif user_input==3:
            print("you have opted exit ")
            print("THANK YOU")

i=interface()


        
# print("====================================")
# print(" Personal Finance Analytics System")
# print("====================================")
# print("REGISTER ")
# print("LOGIN")
# print("EXIT")
# options=["REGISTER ","LOGIN","EXIT"]
# user_input=int(input("enter your choice :"))
