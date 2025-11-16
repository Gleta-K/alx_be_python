Task = input("Enter your task:" )
TimeBound = input("Is it time-bound? (yes/no):" )
Priority = input("Priority (high/medium/low):" )
match Priority:
    case "high":
        reminder = f" '{Task}' is a high priority task"
    case "medium":
        reminder = f" '{Task}' is a medium priority task"
    case "low":
        reminder = f" '{Task}' is a low priority task"
if TimeBound == "yes":
    reminder += f" that requires immediate attention today!"
else:
    reminder += f" Consider completing it when you have free time today"
print(reminder)