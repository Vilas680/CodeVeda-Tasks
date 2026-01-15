import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task_name = input("Enter task name: ")
    task = {
        "id": len(tasks) + 1,
        "title": task_name,
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    for task in tasks:
        print(f"{task['id']}. {task['title']} [{task['status']}]")

def mark_done(tasks):
    try:
        task_id = int(input("Enter task id to mark done: "))
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "Done"
                save_tasks(tasks)
                print("Task marked as done")
                return
        print("Task not found")
    except:
        print("Invalid input")

def delete_task(tasks):
    try:
        task_id = int(input("Enter task id to delete: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
                print("Task deleted")
                return
        print("Task not found")
    except:
        print("Invalid input")

def main():
    tasks = load_tasks()
    while True:
        print("\n1.Add Task 2.View Tasks 3.Mark Done 4.Delete Task 5.Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

main()
