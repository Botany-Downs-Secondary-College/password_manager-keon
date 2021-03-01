#password_manager.py
#create and display password for users
#Keon.C, Feb 22

member_list = []
pass_list = []

 
#add password 
def add_pass():
    repeat =  True
    while repeat == True:
        
        add = input("Enter password here. Type 'end' to return to menu")
        if add == 'end':
            repeat = False
        else:
            pass_list.append(add)
            print("- {} has been added.".format(add))

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

    
        
mode = input("Choose a mode by entering the number:")
while True :
    print("1: Add a task")
    print("2: View list")
    print("3: Exit")

    if mode == '3':
        break
    elif mode == '1':
        add_pass()
    elif mode == '2':
        view_pass()
    else:
        print("Invalid number, please try again.")
        
print("Thank you for using password manager, have a nice day.")
