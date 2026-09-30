print("Simple To do list")

print("""1- Add tasks
2- View tasks
3- Update tasks
4- Delete tasks
5- Mark tasks as completed 
6- Exit """)

option = int(input("What you want to perform : "))

def add_task():
    tasks = input("Enter tasks : ").split(" ")

def view_task():
    print("Your tasks are")    

if option == 1:
    add_task()
elif option == 2:
    view_task()
elif option == 6:
    exit(0)
else:
    print("Invalid")