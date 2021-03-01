#password_manager.py
#create and display password for users
#Keon.C, Feb 22

member_list = []
pass_list = []

 
#add password 
def add_pass():

    while True:
        add_pass = input("Type 'end' to return to menu or Create password with at least 8 characters, 1 Capital letter and a number:").strip()
        if (any(passreqr.isupper() for passreqr in add_pass) and any(passreqr.isdigit() for passreqr in add_pass) and len(add_pass) >=8):
            pass_list.append(add_pass)
            print("- {} has been added.".format(add_pass))
        elif add_pass == 'end':
            break  
        else:
            print("Your password dose not meet the requirements. Please try again.")
            

#view_password
def view_pass():
    print("Here is your passwords.", pass_list)


name = input("What's your name?")
while True:
    try:
        age = float(input("How old are you?"))
        break
    except:
        print("Please enter a integer")
        

print("Welcome to Password Manager.")
if age < 13:
        
    print("Are you a little bit young to use a password manager?")
    exit()
        
if age >= 13:
        
    print("You may proceed")
    repeat = True
    while repeat == True:
            
        member = input("Type LOGIN to login to existing account; Type CREATE to create a new account").upper()
        if member == "LOGIN":
            username = input("PLease enter your username:")
            m_password = input("Please enter your password")
            if username =="bdsc" and m_password =="Pass1234":
                print("Welcome back.")
                repeat = False
            else:
                print("Invalid username or password, please try again")
            
                
        elif member == "CREATE":
            username = input("Create a username:")
                
            while True:
                m_password = input("Create password with at least 8 characters, 1 Capital letter and a number:").strip()
                if (any(passreqr.isupper() for passreqr in m_password) and any(passreqr.isdigit() for passreqr in m_password) and len(m_password) >=8):
                    member_list.append([username, m_password])
                    print("Account created, welcome", username)
                    repeat = False
                    break
                else:
                    print("Your password dose not meet the requirements. Please try again.")

    
        

while True :
    print("1: Add password")
    print("2: View password list")
    print("3: Exit")
    mode = input("Choose a mode by entering the number:")

    if mode == '3':
        break
    elif mode == '1':
        add_pass()
    elif mode == '2':
        view_pass()
    else:
        print("Invalid number, please try again.")
        
print("Thank you for using password manager, have a nice day.")
