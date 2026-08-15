from getpass import getpass

import mypkg.services.file_manager as F
import mypkg.services.sessions as S


SPECIAL_CHARACTERS = "!@#$%^&*"


def CheckCurrentPassword():
    current_user = S.get_current_user()
    data = F.load_users()

    old_password = getpass("Enter your previous password: ")

    return data[current_user]["password"] == old_password


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


def UpdatePassword(new_password):
    current_user = S.get_current_user()
    data = F.load_users()

    data[current_user]["password"] = new_password

    F.save_users(data)


def ChangePasswordSystem():
    if not CheckCurrentPassword():
        print("Old password is incorrect.")
        return False

    new_password = ValidateNewPassword()

    if new_password is None:
        return False

    UpdatePassword(new_password)

    print("Password changed successfully.")
    return True