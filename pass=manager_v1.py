#List
todo_list = []
#Add tasks to to do list
def add_tasks():
    repeat =  True
    while repeat == True:
        add = input("Enter the task to add or type 'end' to return to menu")
        if add == 'end':
            repeat = False
        else:
            todo_list.append(add)
            print("- {} has been added.".format(add))

#View current to do list
def view_tasks():
    print("Here is your to do list.", todo_list)


#Menu
name = input("Please enter name.")
print("Hello there,", name," this is your to do list program, select the options below to begin")
repeat = True     
while repeat ==True :
   
    print("1: Add a task")
    print("2: View list")
    print("3: Exit")
    list = input("Choose a mode by entering the number:")
            
    if list == '3':
        repeat = False
    elif list == '1':
        add_tasks()
    elif list == '2':
        view_tasks()
        
