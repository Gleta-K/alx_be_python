task = input("Enter your task: " )
time_bound = input("Is it time-bound? (yes/no): " )
priority = input("Priority (high/medium/low): " )
match priority:
    case "high":
        reminder = f" '{task}' is a high priority task"
    case "medium":
        reminder = f" '{task}' is a medium priority task"
    case "low":
        reminder = f" '{task}' is a low priority task"
if time_bound == "yes":
    reminder += f" that requires immediate attention today!"
else:
    reminder += f" Consider completing it when you have free time today"
print("\nReminder: ", reminder)