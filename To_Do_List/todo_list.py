tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n--- YOUR TASKS ---")

            for index, item in enumerate(tasks, start=1):
                status = "Completed" if item["completed"] else "Not Completed"
                print(f"{index}. {item['task']} - {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            task_number = int(input("Enter the task number to mark as completed: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            task_number = int(input("Enter the task number to delete: "))

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f"Task '{deleted_task['task']}' deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        with open("tasks.txt", "w") as file:
            for item in tasks:
                file.write(f"{item['task']} - {item['completed']}\n")

        print("Tasks saved successfully!")
        print("Thank you for using the To-Do List!")
        break