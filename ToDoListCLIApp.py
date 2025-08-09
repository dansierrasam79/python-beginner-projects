def show_menu():
    print("\nTo-Do App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.")
    else:
        print("Empty task not added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
        return
    print("\nTasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def edit_task(tasks):
    if not tasks:
        print("No tasks to edit.")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to edit: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the new description: ").strip()
            if new_task:
                tasks[task_num - 1] = new_task
                print("Task updated.")
            else:
                print("Empty task description not saved.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do App. Bye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

