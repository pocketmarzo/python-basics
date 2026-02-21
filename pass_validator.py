PASSWORD_BLACKLIST = ["password", "password123", "admin", "qwerty", "qwerty1234"]

def main():
    
    while True:
        try:
            password = input("Enter your password or 'run' for exit: ").strip()

            if password == "run":
                print("Program finished.")
                break

            is_valid, message = check_password(password)
            
            if is_valid:
                print("Password Accepted")
            else:
                print(message)

        except EOFError:
            print("\nInput interrupted. Please try again.")
        except Exception as e:
            print(f"Something wrong: {e}")


def check_password(user_password):
    if len(user_password) < 8:
        return False, "Password too short"

    if user_password.lower() in PASSWORD_BLACKLIST:
        return False, "The password is too predictable"

    has_digit = any(char.isdigit() for char in user_password)
    has_special = any(char in "!@#$%^&*()-_=+" for char in user_password)

    if not has_digit:
        return False, "Password must contain at least one digit"

    if not has_special:
        return False, "Password must contain at least one special character"

    return True, "Password accepted"
    
main()