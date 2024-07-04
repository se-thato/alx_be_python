def task_info():
    task = input("Enter your task: ") 
    priority = input("priority(high/medium/low): ")
    time_bound = input("Is it time-bound?(yes/no): ")
    return task, priority, time_bound

def make_reminder(task, priority, time_bound):
    reminder = f"Reminder: '{task}' is a {priority} priority task "

    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task "
            if time_bound == "yes":
                reminder += "that requires immediate attention today!"
            else:
                reminder += "Consider completing it when you have free time."
            return reminder
        
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task "
            if time_bound == "yes":
                reminder += "that requires immediate attention today!"
            else:
                reminder += "Consider completing it when you have free time."
            return reminder
        
        case "low":
            reminder = f"Note: '{task}' is a low priority task. "
            if time_bound == "yes":
                reminder += "that requires immediate attention today!"
            else:
                reminder += "Consider completing it when you have free time."
            return reminder
    
def main():
    while True:
        task, priority, time_bound = task_info()
        reminder = make_reminder(task, priority, time_bound)
        print(reminder)

        another_task =input("would you like to enter another task? (yes/no): ")
        if another_task != "Yes":
            break
        
        

if __name__ == "__main__":
    main()