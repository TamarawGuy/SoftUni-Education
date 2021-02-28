from math import floor

salary = float(input())
average_grade = float(input())
minimum_wage = float(input())
social_scholarship = 0
excellent_scholarship = 0

if salary < minimum_wage and average_grade >= 4.5:
    social_scholarship = 0.35 * minimum_wage

if average_grade >= 5.5:
    excellent_scholarship = 25 * average_grade


if social_scholarship > excellent_scholarship:
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")

elif excellent_scholarship > social_scholarship:
    print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")

elif social_scholarship == excellent_scholarship:
    print("You cannot get a scholarship!")