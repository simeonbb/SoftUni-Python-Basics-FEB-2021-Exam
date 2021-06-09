participants = int(input())
count1 = 0
count2 = 0
count3 = 0
count4 = 0

grade_total = 0

for i in range(0, participants):
    grade = float(input())
    if grade >= 5.00:
        count1 += 1
    elif 4 <= grade <= 4.99:
        count2 += 1
    elif 3 <= grade <= 3.99:
        count3 += 1
    else:
        count4 += 1
    grade_total += grade


group1_perc = float(100.00/participants)*count1
group2_perc = float(100.00/participants)*count2
group3_perc = float(100.00/participants)*count3
group4_perc = float(100.00/participants)*count4

avg = grade_total / participants

print(f'Top students: {group1_perc:.2f}%')
print(f'Between 4.00 and 4.99: {group2_perc:.2f}%')
print(f'Between 3.00 and 3.99: {group3_perc:.2f}%')
print(f'Fail: {group4_perc:.2f}%')
print(f'Average: {avg:.2f}')
