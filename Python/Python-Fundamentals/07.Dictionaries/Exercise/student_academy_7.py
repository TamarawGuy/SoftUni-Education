n = int(input())
d_students = {}
d_average = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in d_students:
        d_students[name] = []
        d_students[name].append(grade)
    else:
        d_students[name].append(grade)

for key, value in d_students.items():
    d_students[key] = sum(value) / len(value)

for key, value in d_students.items():
    if d_students[key] >= 4.50:
        d_average[key] = value

sorted_average = dict(sorted(d_average.items(), key=lambda x: x[1], reverse=True))

for key, value in sorted_average.items():
    print(f"{key} -> {value:.2f}")