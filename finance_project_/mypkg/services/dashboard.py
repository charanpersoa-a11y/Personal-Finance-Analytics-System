# this is where the registered or logged in user's dashboard appears
# and after registration user must login for further operations in this project so main thing is i want to fetch the logged in users information to here
# how i will know or how this file will know that a person or a user logged in
# one way is to get a login info here means i the login things will proceed here and directly the info will go to next block of code 
# other way is get the user id while he is logging in and search him in the data base and then get his information from data base
# what this dashboard contains
# 1.the users info like their name email address and all the other transactions in the future

import mypkg.services.auth as a
import mypkg.services.file_manager as f
import mypkg.models.user as u
class Dash():
    def __init__(self,user):
        pass

    def board():
        # your dashboard will be here
        # how i want that dashboard is
        # i want it to display the user info at the top and
        users=f.load_users()
        id=a.Auth.Login()
        user_info=u.User.from_dict(id)
        print(users)
        print(id)

        print(f"name : ")
        print(f"age:")
        print(f"email:")
        print("press something to show your password thing ")
        print("currently your details not available we will update your info later ..")
        # return None





