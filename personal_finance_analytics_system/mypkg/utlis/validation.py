# this helps the programme to get a valid input from the user
from getpass import getpass
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

SPECIAL_CHARACTERS = "!@#$%^&*"
   
def ValidateNewPassword():
    print("Your password must contain:")
    print("- An uppercase letter (A-Z)")
    print("- A lowercase letter (a-z)")
    print("- A number (0-9)")
    print("- A special character (@#$%&)")

    new_password = getpass("Enter your new password: ").strip()

    has_upper = any(char.isupper() for char in new_password)
    has_lower = any(char.islower() for char in new_password)
    has_number = any(char.isdigit() for char in new_password)
    has_special = any(char in SPECIAL_CHARACTERS for char in new_password)

    if not has_upper:
        print("Password needs an uppercase letter.")
        return None

    if not has_lower:
        print("Password needs a lowercase letter.")
        return None

    if not has_number:
        print("Password needs a number.")
        return None

    if not has_special:
        print("Password needs a special character.")
        return None

    confirm_password = getpass("Enter the password again: ").strip()

    if new_password != confirm_password:
        print("Passwords do not match.")
        return None

    return new_password

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