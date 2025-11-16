task = input("Enter your task:" )
time_bound = input("Is it time-bound? (yes/no):" )
priority = input("Priority (high/medium/low):" )
match priority:
    case "high":
        Reminder = f" '{task}' is a high priority task"
    case "medium":
        Reminder = f" '{task}' is a medium priority task"
    case "low":
        Reminder = f" '{task}' is a low priority task"
if time_bound == "yes":
    Reminder += f" that requires immediate attention today!"
else:
    Reminder += f" Consider completing it when you have free time today"
print("\nReminder:", Reminder)