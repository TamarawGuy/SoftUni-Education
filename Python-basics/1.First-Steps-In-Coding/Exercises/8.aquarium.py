length = float(input())
width = float(input())
height = float(input())
percent_occupied_volume = float(input())

volume_of_aquarium = length * width * height
liters_possible = volume_of_aquarium * 0.001
percent = percent_occupied_volume * 0.01
liters_needed = liters_possible * (1-percent)

print(liters_needed)