task = input("Enter your task: ") 
priority = input("priority(high/medium/low): ")
time_bound = input("Is it time-bound?(yes/no): ")

if time_bound = "yes":
    match priority:
        case "high":
            Reminder = f"Reminder: '{task}' is a high priority task "
            if time_bound == "yes":
                Reminder += "that requires immediate attention today! "
            else:
                Reminder += "Consider completing it when you have free time."
            return Reminder
        
        case "medium":
            Reminder = f"Reminder: '{task}' is a medium priority task "
            if time_bound == "yes":
                Reminder += "that requires immediate attention today! "
            else:
                Reminder += "Consider completing it when you have free time."
            return Reminder
        
        case "low":
            Reminder = f"Note: '{task}' is a low priority task."
            if time_bound == "yes":
                Reminder += "that requires immediate attention today!"
            else:
                Reminder += "Consider completing it when you have free time."
            return Reminder
    
