# Initialize an empty list to store tasks
todo_list = []

# Main loop for user interaction
while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    # Add a task
    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print(f"Task '{task}' added to the To-Do list.")

    # View tasks
    elif choice == "2":
        if not todo_list:
            print("No tasks in your To-Do list.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")

    # Remove a task
    elif choice == "3":
        if not todo_list:
            print("No tasks to remove.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")
            
            task_name = input("Enter the exact task name to remove: ")
            if task_name in todo_list:
                todo_list.remove(task_name)
                print(f"Task '{task_name}' removed from the To-Do list.")
            else:
                print("Task not found. Make sure you enter the exact task name.")

    # Exit the program
    elif choice == "4":
        print("Exiting To-Do List program.")
        break

    else:
        print("Invalid choice. Please choose between 1-4.")
