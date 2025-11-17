#Welcome message
print("Welcome to my Python program!")
#Ask for input 
hours = input("How many hours did you study today? ")
#convert input and perform calculations
hours = float(hours)
weekly_hours = hours * 7
#Display the result
print(f"You are on track to study {weekly_hours} hours this week.")
#Add simple error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
  
