d_students = {}
d_count = {}

while True:
    command = input().split(" : ")

    if command[0] == 'end':
        break

    course = command[0]
    student = command[1]

    if course not in d_students:
        d_students[course] = []
        d_students[course].append(student)
        d_count[course] = 1
    elif course in d_students:
        d_students[course].append(student)
        d_count[course] += 1
    
sorted_d_count = dict(sorted(d_count.items(), key=lambda x: x[1], reverse=True))

for key, value in d_students.items():
    d_students[key] = list(sorted(value))

for key, value in sorted_d_count.items():
    print(f"{key}: {sorted_d_count[key]}")
    for people in d_students[key]:
        print(f"-- {people}")