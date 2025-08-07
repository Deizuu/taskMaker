def addTask(taskName:str, taskList:list):
    '''meaning of the 'list.append()' below:
    len(list)+1: refers to the task number (identifier for each task, automatically set relative to the "taskList" list parameter)
    taskName: refers to the name of the task, usually set by the user
    False: refers to the task completion (if the task is completed or not)
    '''
    taskTemplate = [len(taskList)+1, taskName, False]
    taskList.append(taskTemplate)

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

def boolToReadable(boolean:bool):
    if boolean:
        return "Completed"
    else:
        return "Not completed"