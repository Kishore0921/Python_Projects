import os

# Configuration for data persistence
FILE_NAME = "todo_list.txt"

def load_tasks():
    """Loads tasks from a text file into a dictionary format."""
    tasks = {}
    if not os.path.exists(FILE_NAME):
        return tasks
    
    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            # Format in file: Task Name|Status (True/False)
            parts = line.split("|")
            if len(parts) == 2:
                task_name, status_str = parts
                tasks[task_name] = status_str == "True"
    return tasks

def save_tasks(tasks):
    """Saves the current dictionary of tasks to the text file."""
    with open(FILE_NAME, "w") as file:
        for task_name, completed in tasks.items():
            file.write(f"{task_name}|{completed}\n")

def display_menu():
    """Prints the application menu options."""
    print("\n" + "="*30)
    print("      8?? TO-DO LIST MENU      ")
    print("="*30)
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
    print("="*30)

def add_tasks(tasks):
    """Adds one or multiple space-separated tasks to the list."""
    user_input = input("\nEnter tasks to add (separate multiple items with spaces): ").strip()
    if not user_input:
        print("❌ Task name cannot be empty.")
        return
    
    # Split by spaces to handle multiple tasks at once
    new_items = user_input.split()
    added_count = 0
    
    for item in new_items:
        # Avoid duplicate tasks to maintain index integrity
        if item in tasks:
            print(f"⚠️ Task '{item}' already exists. Skipped.")
        else:
            tasks[item] = False
            added_count += 1
            
    if added_count > 0:
        save_tasks(tasks)
        print(f"✅ Successfully added {added_count} task(s)!")

def view_tasks(tasks):
    """Displays all tasks with their current completion status."""
    if not tasks:
        print("\n📭 Your to-do list is empty.")
        return []
    
    print("\n📋 Current Tasks:")
    task_list = list(tasks.keys())
    for index, task in enumerate(task_list, 1):
        status = "✅ Completed" if tasks[task] else "❌ Pending"
        print(f"{index}. {task} [{status}]")
    return task_list

def get_valid_index(task_list, action_name):
    """Helper function to validate user index selection."""
    try:
        choice = int(input(f"Enter the task number to {action_name}: "))
        if 1 <= choice <= len(task_list):
            return choice - 1
        print("❌ Invalid number. Please select an index from the list.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
    return None

def update_task(tasks):
    """Modifies the name of an existing task."""
    task_list = view_tasks(tasks)
    if not task_list:
        return
        
    idx = get_valid_index(task_list, "update")
    if idx is not None:
        old_name = task_list[idx]
        new_name = input(f"Enter new name for '{old_name}': ").strip()
        
        if not new_name:
            print("❌ Task name cannot be empty.")
            return
        if new_name in tasks:
            print("❌ A task with that name already exists.")
            return
            
        # Retain completion status while swapping keys
        tasks[new_name] = tasks.pop(old_name)
        save_tasks(tasks)
        print(f"🔄 Task updated from '{old_name}' to '{new_name}'.")

def delete_task(tasks):
    """Removes a specific task from the list."""
    task_list = view_tasks(tasks)
    if not task_list:
        return
        
    idx = get_valid_index(task_list, "delete")
    if idx is not None:
        removed_task = task_list[idx]
        del tasks[removed_task]
        save_tasks(tasks)
        print(f"🗑️ Task '{removed_task}' successfully deleted.")

def complete_task(tasks):
    """Marks a selected pending task as completed."""
    task_list = view_tasks(tasks)
    if not task_list:
        return
        
    idx = get_valid_index(task_list, "mark as completed")
    if idx is not None:
        selected_task = task_list[idx]
        if tasks[selected_task]:
            print(f"ℹ️ Task '{selected_task}' is already completed.")
        else:
            tasks[selected_task] = True
            save_tasks(tasks)
            print(f"🎉 Task '{selected_task}' marked as completed!")

def main():
    """Main execution loop for the terminal application."""
    tasks = load_tasks()
    
    while True:
        display_menu()
        try:
            option = int(input("What would you like to perform? (1-6): "))
        except ValueError:
            print("❌ Invalid option. Please type a number between 1 and 6.")
            continue
            
        if option == 1:
            add_tasks(tasks)
        elif option == 2:
            view_tasks(tasks)
        elif option == 3:
            update_task(tasks)
        elif option == 4:
            delete_task(tasks)
        elif option == 5:
            complete_task(tasks)
        elif option == 6:
            print("\n👋 Data saved safely. Exiting application. Goodbye!")
            break
        else:
            print("❌ Out of range. Please choose a number from 1 to 6.")

if __name__ == "__main__":
    main()
