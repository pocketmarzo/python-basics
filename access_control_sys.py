

access_db = {
"adis": "admin", 
"mark": "user",
"lilly": "guest",
"jade": "manager"

}

def show_users():

    if not access_db:
        return "The database is empty"
    
    box = ""
    for name in access_db:
        box += f"[USER] {name} | ROLE: {access_db[name]}\n"
    return box
        
    
def add_user(name, role):
    access_db[name] = role
    return f"User '{name}' added with role '{role}'"

def remove_user(name):

    if name in access_db:       
        del access_db[name]
        return f"User '{name}' has been deleted"
    else:
        return "User not found"
        
def main():
    try:
        while True:
            print("1. List| 2. Add| 3. Delete| 4. Exit")
            menu = input("Enter number:").strip().lower()
            
            if menu == "1":
                show = show_users()
                print(show)
            elif menu == "2":
                add_name = input("Enter your name: ").strip().lower()
                add_role = input("Your role: ").strip().lower()
                add = add_user(add_name, add_role)
                print(add)
                
            elif menu == "3":
                del_user = input("Enter user name for remove: ")              
                names_list = del_user.split(",")

                for n in names_list:
                    clean_name = n.strip().lower()
                    result = remove_user(clean_name)
                
                print(result)

            elif menu == "4":
                print("Program finished")
                break
            else:
                print("Ivalid input. Try again")

    except:
        print("Invalid input. Please enter a number from 1 to 4.")

main()