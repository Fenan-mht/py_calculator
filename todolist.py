tasks = []

def AddTask(taskList, task):
    taskList.append(task)

def DeleteTask(taskList, no):
    no_ = int(no)
    NumberToDelete = no_ - 1
    taskList.pop(NumberToDelete)

def DisplayTasks(tasks):
    count = 0
    for n in tasks:
        count += 1
        print(f"{count}. {n}\n\n")

while True:
    print("Welcome to python to-do list\n")
    print("Please Input the numbers to do what you want\n")
    print("1. Add Task\n")
    print("2. Delete Task\n")
    print("3. View Task\n")

    selected = int(input(">>"))

    if selected == 1:
        print("Write 'finish' when you are done listing tasks")
        while True:
            task = input("Add task here: ")
            if task.lower() != "finish":
                print("Added Task", task)
                AddTask(tasks, task)
            if task.lower() == "finish":
                print("Finished Adding Task!")
                break

    elif selected == 2:
        if len(tasks) == 0:
            print("There are no tasks to be deleted, add tasks first")
            selected = 1
        else:
            print("Write '999' when you are done deleting tasks")
            while True:
                taskNumber = int(input("Which Number would you like to delete"))
                if taskNumber != 999 and taskNumber <= len(tasks):
                    DeleteTask(tasks, taskNumber)
                if len(tasks) == 0:
                    print("No tasks remaining. Setting selected back to 1.")
                    selected = 1
                    break
                elif taskNumber == 999:
                    print("Finished deleting tasks")
                    break
                else:
                    print("Invalid number, please try again!")

    elif selected == 3:
        if len(tasks) == 0:
            print("There are no tasks.")
        DisplayTasks(tasks)
    else:
        print("Invalid selection. Please choose a number between 1 and 3.\n")
