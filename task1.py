# To Do list creater.
# Saathvik Alkanti / CodSoft Intern Task 1

todo_list = []

while True:
    
    print("\nTo-Do List Menu")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Quit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        if not todo_list:
            print("No tasks yet.")
        else:
            print("Your tasks:")
            for i, task in enumerate(todo_list, 1):
                print(str(i) + ". " + task)

    elif choice == "2":
        task = input("Enter your task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Please enter 1, 2, or 3.")
