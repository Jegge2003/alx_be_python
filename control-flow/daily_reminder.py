task = input("Enter a task description: ")
priority = input("Enter task's priority (high, medium, low): ")
time_bound = input("Is the task time bound? (yes or no)")

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a {priority} priority task. Consider completing it at your free time.")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today")
        else:
            print(f"Reminder: {task} is a {priority} priority task. Consider completing it at your free time.")
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today")
        else:
            print(f"Reminder: {task} is a {priority} priority task. Consider completing it at your free time.")
    case _:
        print('You will have to choose from the alternatives given')
