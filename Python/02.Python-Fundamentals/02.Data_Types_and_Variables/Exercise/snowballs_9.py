n = int(input())
value = 0
for i in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    if (snowball_snow / snowball_time) ** snowball_quality > value:
        snow = snowball_snow
        time = snowball_time
        quality = snowball_quality 
        value = (snowball_snow / snowball_time) ** snowball_quality
    
print(f"{snow} : {time} = {int(value)} ({quality})")