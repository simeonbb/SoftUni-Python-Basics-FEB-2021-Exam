daily_goal = int(input())
result = 0
price = 0
command = input()
while command != 'closed' or result != daily_goal:
    current_command = command
    if current_command == 'haircut mens':
        price = 15
        result += price
    elif current_command == 'haircut ladies':
        price = 20
        result += price
    elif current_command == 'haircut kids':
        price = 10
        result += price

    if current_command == 'color touch up':
        price = 20
        result += price
    elif command == 'color full':
        price = 30
        result += price
    command = input()

if result >= daily_goal:
    print("You have reached your target for the day!")
else:
    print(f'Target not reached! You need {daily_goal - result}lv. more.')

print(f'Earned money: {result}')
