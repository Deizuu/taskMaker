# Import functions
import taskManagerFunctions as tmf

# If this variable is True, the program will keep running.
running = True

# The list that will contain all tasks
allTasks = []

while(running):
    print("1: Add a task \n2: Show task list \n3: Complete/uncomplete a task \n4: Rename a task \n5: Exit the program")
    # Registers the user's input
    user_input = str(input("Press 1, 2, 3, 4 or 5: "))

    match user_input:
        case '1':
            tmf.addTask(input("Enter the name of the task: \n"), allTasks)
            print("\n")

        case '2':
            print("\nHere are your tasks:\n")
            for task in allTasks:
                print(f"{task[0]}. {task[1]} | {"Completed" if task[2] else "Uncompleted"} \n")
            #tmf.listTasks(allTasks)
            #print(allTasks)
            
        case '3':
            tmf.listTasks(allTasks)
            tmf.toggleTaskCompletion(allTasks, int(input("What task do you want to mark as completed ? (enter task number): ")))
            print("\n")

        case '4':
            tmf.listTasks(allTasks)
            tmf.renameTask(allTasks, int(input("Which task do you want to rename ? (enter task number): ")), input("Enter new name for task: "))
            print("\n")

        case '5':
            running = False