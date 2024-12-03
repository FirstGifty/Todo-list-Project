import json
import os

TODO_FILE = 'todo_list.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Not done"
            print(f"{idx}. {task['task']} - {status}")

def update_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["task"] = input("Enter the new task: ")
        tasks[task_num]["done"] = input("Is the task done? (yes/no): ").strip().lower() == 'yes'
        save_tasks(tasks)
        print("Task updated!")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        save_tasks(tasks)
        print("Task deleted!")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTodo List Manager")
        print("1. Enter task")
        print("2. Show all tasks")
        print("3. Update task")
        print("4. Remove task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            enter_task(tasks)
        elif choice == '2':
            show_all_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
