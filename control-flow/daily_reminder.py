task = input("Input a task description:" )
priority = input("Enter task's priority (high/medium/low):" )
TimeBound = input("Is the task time-bound? (yes/no):" )
match priority:
    case "high":
        print("'", task, "' is a high priority task that requires immediate attention today!")
    case "medium":
        print("'", task, "' is a medium priority task. Consider completing it after you're done with the high priority tasks for the day!")
    case "low":
        print("'", task, "' is a low priority task. Consider completing it when you have free time.")
if TimeBound == "yes":
    print("This is also a time-bound task. Complete it as a soon as possible!")