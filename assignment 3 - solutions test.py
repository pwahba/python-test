# annual_salary = float(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# total_cost = float(input("Enter the cost of your dream home: "))
# semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
# portion_down_payment = total_cost * 0.25
# monthly_salary = annual_salary/12
# portion_saved_monthly = monthly_salary * portion_saved
# current_savings = 0
# months = 0
# while current_savings < portion_down_payment:
#     current_savings = current_savings + (current_savings*(0.04/12)) + portion_saved_monthly
#     months = months + 1 
#     if months % 6 == 0:
#         annual_salary = annual_salary + (annual_salary*semi_annual_raise)
#         monthly_salary = annual_salary/12
#         portion_saved_monthly = monthly_salary * portion_saved

print("Number of months: ", months)

#-------------------------------------------------------------------------------------

annual_salary = float(input("Please share your annual salary: "))
# portion_saved = float(input("How much of your salary you can save? (Please enter a number in decimal, for example: 0.1 for 10%): "))
total_cost = 1000000
semi_annual_raise = 0.07
down_payment_percentage = 0.25
portion_down_payment = down_payment_percentage * total_cost
monthly_salary = annual_salary / 12
annual_r = 0.04 / 12
# monthly_salary_saved = portion_saved * monthly_salary

current_savings = 0
months = 0
# error_margin = portion_down_payment - 100

# while current_savings <= portion_down_payment:
#     current_savings += monthly_salary_saved + current_savings * annual_r
#     months += 1
#     if months % 6 == 0:
#         annual_salary += annual_salary * semi_annual_raise
#         monthly_salary = annual_salary / 12
#         monthly_salary_saved = monthly_salary * portion_saved

print("Your yearly saving plus the investment would be: $", round(current_savings))
print("It will take you around", months, "months to pay a total down payment of $", portion_down_payment)