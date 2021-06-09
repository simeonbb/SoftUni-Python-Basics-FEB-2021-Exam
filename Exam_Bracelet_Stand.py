budget = float(input())
daily_profits = float(input())
expenses = float(input())
gift_price = float(input())

budget_After_5_days = 5 * budget
profits_total = 5 * daily_profits
total_savings = budget_After_5_days + profits_total

total_savings -= expenses

if total_savings >= gift_price:
    print(f'Profit: {total_savings:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {gift_price - total_savings:.2f} BGN.')