d_results = {}
d_submissions = {}

while True:
    line = input().split("-")

    if line[0] == 'exam finished':
        break

    if len(line) == 3:
        username = line[0]
        language = line[1]
        points = int(line[2])

        if username not in d_results:
            d_results[username] = points
        else:
            if d_results[username] < points:
                d_results[username] = points
        
        if language not in d_submissions:
            d_submissions[language] = 1
        else:
            d_submissions[language] += 1

    elif len(line) == 2:
        username = line[0]

        if username in d_results:
            del d_results[username]
        
sorted_results = dict(sorted(d_results.items(), key=lambda x: (-x[1], x[0])))
sorted_submissions = dict(sorted(d_submissions.items(), key=lambda x: (-x[1], x[0])))

print("Results:")

for key, value in sorted_results.items():
    print(f"{key} | {value}")

print("Submissions:")

for key, value in sorted_submissions.items():
    print(f"{key} - {value}")