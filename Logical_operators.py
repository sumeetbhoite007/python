# and or not are the logical operators

try:
    income = input("What is your monthly income? ")
    if not income.isdigit():
        raise ValueError ("Invalid format. Please enter a numeric value for income.")
    income = int(income)
    
    credit = input("What is your credit score? ")
    if not credit.isdigit():
        raise ValueError("Invalid format. Please enter a numeric value for credit score.")
    credit = int(credit)
    
    student = input("Are you a student? y/n: ").strip().lower()
    if student not in ("y", "n"):
        raise ValueError("Please enter the answer only in 'y' or 'n'.")
    
    if (income >= 50000 or credit >= 750) and student == "n":
        print("Eligible for loan.")
    else:
        print("Not eligible for loan.")
        
except ValueError as e:
    print(e)
        
        
    