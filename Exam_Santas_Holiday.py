days_in = int(input())
type_of_room = input()
grade = input()
discount = 0
price_per_night = 0
total = 0

if type_of_room == 'room for one person':
    discount = discount
    price_per_night = 18.00
    total = (days_in-1) * price_per_night
    if grade == 'positive':
        total = total + (total*0.25)
    else:
        total = total - (total*0.10)

elif type_of_room == 'apartment':
    if days_in < 10:
        discount = 0.30
    elif 10 <= days_in <= 15:
        discount = 0.35
    else:
        discount = 0.50

    price_per_night = 25.00
    total = (days_in-1) * price_per_night
    total = total - (discount * total)

    if grade == 'positive':
        total = total + (total*0.25)
    else:
        total = total - (total*0.10)

elif type_of_room == 'president apartment':
    if days_in < 10:
        discount = 0.10
    elif 10 <= days_in <= 15:
        discount = 0.15
    else:
        discount = 0.20

    price_per_night = 35.00
    total = (days_in-1) * price_per_night
    total = total - (discount * total)

    if grade == 'positive':
        total = total + (total*0.25)
    else:
        total = total - (total*0.10)


print(f'{total:.2f}')
