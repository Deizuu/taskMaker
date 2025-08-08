def addTask(taskName:str, taskList:list) -> int:
    '''Template explanation:
    len(list)+1: refers to the task number (identifier for each task, automatically assigned relative to the "taskList" list length)
    taskName: refers to the name of the task
    False: refers to the task completion (if the task is completed or not)
    '''
    taskTemplate = [len(taskList)+1, taskName, False]
    # Boolean value for checking if a task with the name taskName does not already exist
    newName = True
    for task in taskList:
        if task[1] == taskName:
            newName = False
    if newName:
        taskList.append(taskTemplate)
    else:
        # 1: Task not created, because name is taken
        return 1
    # 0: Task created successfully
    return 0

def toggleTaskCompletion(taskList:list, taskNumber:int):
    for task in taskList:
        # Changes task completion value to 'True' if the value was previously set to 'False'
        if task[0] == taskNumber and task[2] == False:
            task[2] = True

        # Changes task completion value to 'True' if the value was previously set to 'False'
        elif task[0] == taskNumber and task[2] == True:
            task[2] = False

def renameTask(taskList:list, taskNumber:int, newTaskName:str):
    for task in taskList:
        if task[0] == taskNumber:
            task[1] = newTaskName