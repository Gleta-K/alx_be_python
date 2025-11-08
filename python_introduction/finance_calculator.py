monthly_income = int(input("Enter your monthly income:" ))
monthly_expenses = int(input("Enter your total monthly expenses" ))
R = 0.05 # R is the simple interest rate
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are $",monthly_savings)
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: $",int(projected_savings))