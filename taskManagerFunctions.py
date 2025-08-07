import os
def addTask(taskName:str, list:list):
    '''The three values are:
    1st value: task number
    2nd value: task name
    3rd value: task completion (False = uncompleted ; True = completed)'''
    list.append([len(list)+1, taskName, False])
def completeTask(taskList:list, taskNumberSearch:int):
    for element in list:
        if element[0] == taskNumberSearch:
            element[2] = True
def boolToReadable(boolean:bool):
    if boolean:
        return "Completed"
    else:
        return "Not completed"
def listTasks(taskList:list):
    print("Here are your tasks:")
    for task in taskList:
        print(f"{task[0]}. {task[1]} | {boolToReadable(task[2])} \n \n")