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










