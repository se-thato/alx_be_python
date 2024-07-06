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
    
<<<<<<< HEAD
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
=======
>>>>>>> 0fb3134941deda1b110b2a197becd4243b5a92b4
