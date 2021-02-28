from math import floor

record_in_seconds = float(input())
distance = float(input())
seconds_1_meter = float(input())

distance_seconds = distance * seconds_1_meter
additional_seconds_from_water = floor(distance / 15)
additional_seconds_from_water *= 12.5
total_seconds = distance_seconds + additional_seconds_from_water

if total_seconds >= record_in_seconds:
    seconds_slower = total_seconds - record_in_seconds
    print(f"No, he failed! He was {seconds_slower:.2f} seconds slower.")

else:
    print(f"Yes, he succeeded! The new world record is {total_seconds:.2f}")