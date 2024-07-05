task = input("Enter your task: ") 
priority = input("priority(high/medium/low): ")
time_bound = input("Is it time-bound?(yes/no): ")

if time_bound == "yes":
    match priority:
        case "high":
            print (f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        
        case "low":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
            
        case_:
            print( f"Invalid level please use (high/medium/low)")
    
