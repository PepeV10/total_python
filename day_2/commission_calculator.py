employee_name = input("What is your name?: ")
monthly_sales = input("How much did you sell this month?: $")
commission = 13 / 100
employee_commission = float(monthly_sales) * commission
final_commission = round(employee_commission, 2)
final_commission = "{:.2f}".format(employee_commission)
print(f"Your commission for the month is ${final_commission}, congratulations")
