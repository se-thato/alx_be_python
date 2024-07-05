task = input("Enter your task: ") 
priority = input("priority(high/medium/low): ")
time_bound = input("Is it time-bound?(yes/no): ")

if time_bound = "yes":
    match priority:
        case "high":
            return f"Reminder: '{task}' is a high priority task that requires immediate attention toda
        
        case "low":
            return f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
            
        else:
            return f"Invalid level please use (high/medium/low)"
    
