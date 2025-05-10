import json
import os

TODO_FILE = "todo_list.json"

# Load tasks from file if exists
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks in your list.\n")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{idx}. [{status}] {task['task']}")
        print()

# Add a new task
def add_task(tasks):
    task_desc = input("Enter the new task: ").strip()
    if task_desc:
        tasks.append({"task": task_desc, "done": False})
        print("Task added!\n")
    else:
        print("Empty task not added.\n")

# Mark a task as done
def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as done.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Enter a valid number.\n")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task: {removed['task']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Enter a valid number.\n")

# Main loop
def main():
    tasks = load_tasks()
    
    while True:
        print("To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
