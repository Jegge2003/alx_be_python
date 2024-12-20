task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

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
