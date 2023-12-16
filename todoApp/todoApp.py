#Simple To-Do Terminal app
import random

def show_tasks(Tasks):
    """Displays tasks available"""
    print("Tasks: ")
    if len(Tasks) > 0:
        for key, value in Tasks.items():
            print(f"{key}. {value}")
    print("\n")


def key_gen(keys):
    """Generates a unique key each time it is called"""
    # if len(keys) == 1:
    #     return 1
    key = max(keys, default = 0) +1
    return key


def add_task(Tasks,keys,task_description):
    key = key_gen(keys)
    keys.append(key)
    Tasks[key] = task_description
    return Tasks, keys

def update_tasks(Tasks,keys):
    """Updates keys of the dictionary after task is removed"""
    starting_key = key_gen(keys)
    new_tasks = {starting_key+i:value for i,value in enumerate(Tasks.values())}
    return new_tasks


def remove_task(Tasks,key,keys):
    """Removes the specified task"""
    Tasks.pop(key)
    keys.remove(key)
    return update_tasks(Tasks,keys),keys
    

def get_tasks_description():
    """Asks the user to enter task description"""
    task_desc = input("Enter task description: ")
    return task_desc


def edit_task(Tasks,key):
    "Edits the task"
    print("Please re-enter the entire task description for now.")
    new_desc = get_tasks_description()
    Tasks.update({key:new_desc})
    return Tasks


def main():
    Tasks = dict()
    keys = []
    while True:
        show_tasks(Tasks)
        print("1. Add task")
        print("2. Edit task ")
        print("3. Remove task")
        print("4. Exit")
        choice = input("> ").strip()

        if choice == '1':
            task_description = get_tasks_description()
            Tasks, keys = add_task(Tasks,keys,task_description)
            show_tasks(Tasks)
            print("\n")
        elif choice == '2':
            index = int(input("Enter task number: "))
            Tasks = edit_task(Tasks,index)
            show_tasks(Tasks)
            print("\n")

        elif choice == '3':
            index = int(input("Enter task number: "))
            Tasks,keys = remove_task(Tasks,index,keys)
            show_tasks(Tasks)
            print("\n")

        elif choice == '4':
            print("Exiting to-do app. Bye!")
            break


if __name__ == "__main__":
    main()








