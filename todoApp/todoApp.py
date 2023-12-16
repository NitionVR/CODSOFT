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
    









