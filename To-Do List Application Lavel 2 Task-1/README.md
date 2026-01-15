To-Do List Application (Python)
📌 Project Description

This project is a Command-Line To-Do List Application developed using Python.
It allows users to add, view, mark as done, and delete tasks.
All tasks are stored permanently in a JSON file, so data is not lost after closing the program.

🎯 Objectives

Create a menu-driven program
Perform CRUD operations on tasks
Store tasks in a JSON file
Implement basic error handling
Understand file handling in Python

🛠 Technologies Used

Programming Language: Python
Data Storage: JSON
IDE: VS Code / PyCharm / IDLE
Platform: Command Line (Terminal)

📂 Project Structure
To-Do List Application/
│
├── todo.py
├── tasks.json
└── README.md

⚙️ How It Works (Step by Step)

Program loads tasks from tasks.json
Displays menu options to the user
User can:

Add a new task
View all tasks
Mark a task as done
Delete a task
Changes are saved automatically to the JSON file
Error messages are shown for invalid inputs

▶️ How to Run the Project

Make sure Python (3.x) is installed
Open terminal in project folder

Run the command:
python todo.py

📥 Menu Options
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Exit

📤 Sample Output
1.Add Task 2.View Tasks 3.Mark Done 4.Delete Task 5.Exit
Choose: 1
Enter task name: Learn Python
Task added successfully

Choose: 2
1. Learn Python [Pending]
