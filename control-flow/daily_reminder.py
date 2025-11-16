description = input("Input a task description:" )
priority = input("Enter task's priority (high/medium/low):" )
time = input("Is the task time-bound? (yes/no):" )
match priority:
    case "high":
        print(description, "is a high priority task that requires immediate attention today!")
    case "medium":
        print(description, "is a medium priority task. Consider completing it after you're done with the high priority tasks for the day!")
    case "low":
        print("'", description, "' is a low priority task. Consider completing it when you have free time.")
if time == "yes":
    print("This is also a time-bound task. Complete it as a soon as possible!")