# daily_reminder.py

def daily_reminder():
    # Get user input for task
    task = input("Enter your task: ")

    # Get user input for priority
    priority = input("Priority (high/medium/low): ").lower()

    # Get user input for time sensitivity
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process task based on priority and time sensitivity
    match priority:
        case "high":
            priority_message = "high priority task"
        case "medium":
            priority_message = "medium priority task"
        case "low":
            priority_message = "low priority task"
        case _:
            print("Invalid priority level.")
            return

    if time_bound == "yes":
        reminder = f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!"
    elif time_bound == "no":
        reminder = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound task.")
        return

    # Print reminder
    print(reminder)

if __name__ == "__main__":
    daily_reminder()
# daily_reminder.py
