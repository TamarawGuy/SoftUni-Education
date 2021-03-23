hour_exam = int(input())
minutes_exam = int(input())
hour_arrival = int(input())
minutes_arrival = int(input())

if hour_exam == hour_arrival :
    # 9:00 and 9:00
    if minutes_exam == minutes_arrival:
        print("On time")
    elif minutes_exam < minutes_arrival:
        minutes_late = minutes_arrival - minutes_exam
        print("Late")
        print(f"{minutes_late:02d} minutes after the start")
    elif minutes_exam > minutes_arrival:
        minutes_early = minutes_exam - minutes_arrival
        print("Early")
        print(f"{minutes_early:02d} minutes before the start")

elif hour_exam > hour_arrival:

    # 9:00 and 8:00
    if minutes_exam == minutes_arrival:
        hours = hour_exam - hour_arrival
        print("Early")
        print(f"{hours}:{minutes:02d} hours before the start")
    
    # 9:00 and 8:45
    elif minutes_exam < minutes_arrival:
        minutes = 60 - minutes_arrival + minutes_exam
        if minutes <= 30:
            print("On time")
        else:
            print("Early")
        print(f"{minutes} minutes before the start")
    
    elif minutes_exam > minutes_arrival:
        hours = hour_exam - hour_arrival
        minutes = minutes_exam - minutes_arrival
        print("Early")
        print(f"{hours}:{minutes:02d} minutes before the start")

elif hour_exam < hour_arrival: 
    # 11:10 and 12:10
    if minutes_exam == minutes_arrival:
        hours = hour_arrival - hour_exam
        print("Early")
        print(f"{hours}:{minutes:02d} hours after the start")
    
    # 11:10 and 12:20
    elif minutes_exam < minutes_arrival:
        hours = hour_arrival - hour_exam
        minutes = minutes_arrival - minutes_exam
        print("Late")
        print(f"{hours}:{minutes:02d} hours after the start")
    
    # 11:30 and 12:20
    elif minutes_exam > minutes_arrival:
        minutes = 60 - minutes_exam + minutes_arrival
        print("Late")
        print(f"{minutes:02d} minutes after the start")
    