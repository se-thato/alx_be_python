monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = total_monthly_expenses - monthly_income

annual_saving = monthly_savings * 12
projected_annual_savings = annual_saving + (annual_saving  * 0.05)

print(f"Your monthly savings are $ {monthly_savings:.2f}. ")
print(f"projected savings after one year, with interest, is: ${projected_annual_savings:.2f}. ")