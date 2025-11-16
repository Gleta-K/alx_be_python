Task = input("Enter your task:" )
TimeBound = input("Is it time-bound? (yes/no):" )
Priority = input("Priority (high/medium/low):" )
match Priority:
    case "high":
        print("'", Task, "' is a high priority task")
        if TimeBound == "yes":
            print("that requires immediate attention today!")
        else:
            print("Consider completing it when you have free time.")
    case "medium":
        print("'", Task, "' is a medium priority task.")
        if TimeBound == "yes":
            print("that requires immediate attention today!")
        else:
            print("Consider completing it when you have free time.")
    case "low":
        print("'", Task, "' is a low priority task. Consider completing it when you have free time.")
        if TimeBound == "yes":
            print("that requires immediate attention today!")
        else:
            print("Consider completing it when you have free time.")