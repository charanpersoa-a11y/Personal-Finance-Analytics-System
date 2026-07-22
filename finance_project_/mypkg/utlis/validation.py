# this helps the programme to get a valid input from the user
def ValidateLimit():
    try:
        limit=int(input("enter the limit value for your budget"))
        if limit>0:
          return limit
        else:
           print("enter a positive number")
    except (ValueError):
       return "please enter a valid number"




def ValidateAge():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 18:
                print("You must be older than 18 to use this program")
                continue
            break
        except ValueError:
            print("Enter a valid number")
    return age

   
def ValidatePassword():
    while True:
        password = input("Set a strong password: ")
        if len(password) <= 6:
            print("Your password must be at least 7 characters long")
            continue
        break

    return  password

def ValidateAmount():
    while True:
        try :
            amount=int(input("enter your amount:-"))
            if amount<0:
                print("amount should be positive .")
                continue
            break
        except Exception as e:
            print(f"an error showed as e")

    return amount