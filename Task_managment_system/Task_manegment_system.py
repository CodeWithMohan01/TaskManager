# function add a heading ling in task file 
def head(name1):
    heading = "\n\t*** tasks ***\n"
    with open(f'{name1}_task.txt','r') as f:
        head_read = f.read()
        if heading in head_read:
            f.close()
        else:
            with open(f'{name1}_task.txt','w') as fs:
                return fs.write(heading)


def wrong_choice(fun_name):
    lst_choice = input("\n\t\tPress 0 for try again: , \n\t\tPress 1 for exit: ")
                
    if lst_choice == '0':
        fun_name
    elif lst_choice == '1':
        exit()
    else:
        print("\n\t\t*** Wrong choice ***")  


# check users login details and login in the system.....
def login():
    id_name = input("\n\t\tEnter your id name for login:- ")
    pswrd = input("\t\tEnter your password:- ")
    with open(f'{id_name}.txt', 'r') as fs:
        passkey = fs.readline(10)
    with open('user_id.txt', 'r') as f:
        user_id = f.read()
        if id_name in user_id:
            print("bug")
            if pswrd in passkey:
                task_manage(id_name)
            else:
                print("\n\t\t<<<<< id pass does not match >>>>>\n\t\t\t*** Try again ***")
                login()
        else:
            print("\n\t\t<<<<< user_id does not exist >>>>>\n\t\t\t*** Try again ***")
            login()



def task_manage(id_name):
    choice1 = input("\n\t\tPress 0 for Enter new task: \n\t\tPress 1 for edit or viwe tasks: ")
  
    if choice1 == '0':
        add_task(id_name)       #call the add_task function for inserting new tasks

    elif choice1 == '1':
        edit_task(id_name)      #call the edit_task function for allow user to make change with tasks

    else:
        print("\n\t\t*** wrong choice! ***\n")
        wrong_choice(task_manage(id_name))


#  this function is insert tasks 
def add_task(name1):
    task_file = input("\n\t\tWrite your task: ")
    head(name1)         # function used for add a heading in task field
    with open(f'{name1}_task.txt','a') as f:
        f.write(f"{task_file}\n")
        # print("done!")
    checkNo = input("\n\t\tPress 0 for if you want to add more: \n\t\tPress 1 for view: \n\t\tpress 2 for exit: ")
    if checkNo == '0':             # here fuction call it self as recursion **line no 29
        add_task(name1)
    elif checkNo == '1':           #call the task inserting function **line no 47
        edit_task(name1)
    elif checkNo == '2':           #terminate or exit program
        exit()
    else:   
        print("\n\t*** wrong choice! ***\n")
        wrong_choice(add_task(name1))


# fuction is used for edit the task
def edit_task(name1):
    with open(f'{name1}_task.txt', 'r') as f:
        tasks = f.read()
        print(f"\n{tasks}")             # print the existing task for check

    choice1 = input("\t\tPress 0 for mark as complete task: \n\t\tPress 1 for edit task: \n\t\tPress 2 for delete task: ")
    
    if choice1 == '0':                        # mark the existing task as completed
        with open(f'{name1}_task.txt','r') as f1:
            task_check = f1.read()
            task_input = input("\n\t\tEnter which you have complete: ")
        #   mark the existing as complited 
            if task_input in task_check:
                with open(f'{name1}_task.txt','w') as f2:
                    f2.write(task_check.replace(task_input, f"{task_input}   **Completed**"))   
            else:
                print("\n\t*** This task is not exist ***")
                wrong_choice(edit_task(name1))
                              

    elif choice1 == '1':                  # call the replace task function **line no 40
        replace_task(name1)
    elif choice1 == '2':
        delete_task(name1)              # call the task deleting function **line no 85
    else:
        print("\n\t\t*** wrong choice! ***\n")
        wrong_choice(edit_task(name1))


# function is used for deleting any existting task
def delete_task(name1):
    with open(f'{name1}_task.txt','r') as f:
            task_check = f.read()
            task_input = input("\n\t\tEnter which you wants to delete: ")
        #   replace the task with null value 
            if task_input in task_check:
                with open(f'{name1}_task.txt','w') as f1:
                    f1.write(task_check.replace(task_input, ""))
                with open(f'{name1}_task.txt','r') as f3:   # print the task after make the change
                    updated_task = f3.read()
                    print(f"\t\t{updated_task}\n")
            else:
                print("\n\t*** This task is not exist ***")
                wrong_choice(delete_task(name1))
       

# this function is used for replace or edit any existing task 
def replace_task(name1):
    old_task = input("Enter task which you want to edit or replace: ")    #take input a old existing task which user wants to edit
    new_task = input("Enter new task you want to update: ")

    with open(f'{name1}_task.txt', 'r') as f:
        task_check = f.read()
        if old_task in task_check:                  # replace or edit any existing task 
            with open(f'{name1}_task.txt', 'w') as f2:
                f2.write(task_check.replace(old_task, new_task))
                edit_task(name1)                    # call edit task function **line no 55
        else: 
            print("\n\t*** This task is not exist ***")
            wrong_choice(replace_task(name1))


# accept new user's data and save in memory as txt file...........
def rgstr(unq_id, name1, work, contect, pswrd):
     
    with open(f'{unq_id}.txt','a') as f:
        f.write(f"{pswrd}\n")        
        f.write(f"{contect}\n")  
        f.write(f"{name1}\n")        
        f.write(f"{work}\n")        
    login()   
     
     
# function check uniqe users id.............
def id_check(unq_id):
    with open('user_id.txt','r') as f:
            name_check = f.read()
            if unq_id in name_check:
                print("\n\t<<<<<This user name already exist try again>>>>>\n")
                details()
            else:
                with open('user_id.txt', 'a') as f:
                    f.writelines(f"{unq_id}\n")


# function ask for singup details from user..................
def details():
    unq_id = input("\t\tEnter your user name:-  ")
    id_check(unq_id)
    name1 = input("\t\tEnter your full name:-  ")
    work = input("\t\tEnter your profession:-  ")
    contect = input("\t\tEnter your contect deteails:-  ")
    pswrd = input("\t\tCreate a storng password:-  ")
    rgstr(unq_id, name1, work, contect, pswrd)
 
def start():
    choice1 = input("\t\tPress 0 for login:- \n\t\tPress 1 for resigter new user:- ")
    if choice1 == '0':    
        login()         # call login fuctoion **line no 2
    elif choice1 == '1':
        details()
    else:
        print("\n\t\t*** wrong choice! ***\n")
        start()


# program starts here >>>>>>>>>>>>>
print("\n\t*** Welcome to task manegment system ***\n")
print("\t\t*** login deteils ***\n")
start()