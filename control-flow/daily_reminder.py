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
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a medium priority task.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority level.")

if __name__ == "__main__":
    daily_reminder()

# daily_reminder.py
# This script allows users to set a daily reminder for tasks with different priorities and time sensitivity.
# It uses a match-case structure to handle different priority levels and time sensitivity.
# The user is prompted to enter a task, its priority, and whether it is time-bound.
# The script then provides appropriate reminders based on the inputs.