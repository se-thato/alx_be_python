monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses

annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}".rstrip('0').rstrip('.')
print(f"Projected savings after one year, with interest, is: ${projected_savings}".rstrip('0').rstrip('.')
