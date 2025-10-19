# To-Do list stored as a list of dictionaries
todo_list = []

# Function to add a new task
def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added.")

# Function to view all tasks
def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
        return
    print("\nTo-Do List:")
    for index, item in enumerate(todo_list, start=1):
        status = "✔️ Done" if item["completed"] else "❌ Not Done"
        print(f"{index}. {item['task']} [{status}]")
    print()

# Function to mark a task as complete
def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
