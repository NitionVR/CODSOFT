#Simple To-Do Terminal app
import random

def show_tasks(Tasks):
    """Displays tasks available"""
    print("Tasks: ")
    if len(Tasks) > 0:
        for key, value in Tasks.items():
            print(f"{key}. {value}")
    print("\n")










