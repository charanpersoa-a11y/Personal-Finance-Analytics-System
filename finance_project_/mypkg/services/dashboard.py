
import mypkg.services.sessions as s
import mypkg.services.auth as a
import mypkg.services.file_manager as f
import mypkg.models.user as u
import mypkg.models.transactions as T
class Dash():

    def board():
        users_id=s.get_current_user()

        users=f.load_users()
        print("==========================================")
        print(f"welcome to your dashboard {users[users_id]["name"]}")

        # self.user_info=u.User.from_dict(users_id)
        print(f"here is your complete details /n{users[users_id]}")
        print(f" your user id is {users_id}")
        print("==========================================")

        print(f"name : {users[users_id]["name"]}")
        print(f"age:{users[users_id]["age"]}")
        print(f"email:{users[users_id]["email"]}")


        print("your transaction history is ")
        


        print("more updated coming soon ......")
        print("==========================================")
        # return None





