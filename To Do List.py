import os
import json

TASKS_FILE = "todo_list.json"

# Load tasks from file if it exists
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task['completed'] else "✗"
        print(f"{i}. [{status}] {task['title']}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added!")

# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        tasks[task_num - 1]['completed'] = True
        print("Task marked as completed.")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        deleted = tasks.pop(task_num - 1)
        print(f"Deleted task: {deleted['title']}")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
