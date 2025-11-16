Task = input("Enter your task:" )
TimeBound = input("Is it time-bound? (yes/no):" )
Priority = input("Priority (high/medium/low):" )
match Priority:
    case "high":
        print("'", Task, "' is a high priority task that requires immediate attention today!")
    case "medium":
        print("'", Task, "' is a medium priority task. Consider completing it after you're done with the high priority tasks for the day!")
    case "low":
        print("'", Task, "' is a low priority task. Consider completing it when you have free time.")
if TimeBound == "yes":
    print("This is also a time-bound task. Complete it as a soon as possible!")