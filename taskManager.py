# Import functions
import taskManagerFunctions as tmf

# If this variable is True, the program will keep running.
running = True

# The list that will contain all tasks
allTasks = []

while(running):

    print("1: Add a task \n2: Show task list \n3: Mark a task as completed \n4: Exit the program")
    # Registers the user's input
    user_input = str(input("Press 1, 2, 3 or 4: "))
    match user_input:
        case '1':
            tmf.addTask(input("Enter the name of the task: \n"), allTasks)
        case '2':
            tmf.listTasks(allTasks)
            print(allTasks)
        case '3':
            tmf.listTasks(allTasks)
            tmf.completeTask(allTasks, int(input("What task do you want to mark as completed ? (enter task number): ")))
        case '4':
            running = False