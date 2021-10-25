class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
    

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1
        

    def get_info(self, species):
        if species == 'mammal':
            return f"Mammals in {self.name}: {', '.join(self.mammals)}", f"Total animals: {Zoo.__animals}"
        if species == 'fish':
            return f"Fishes in {self.name}: {', '.join(self.fishes)}", f"Total animals: {Zoo.__animals}"
        if species == 'bird':
            return f"Birds in {self.name}: {', '.join(self.birds)}", f"Total animals: {Zoo.__animals}"


zoo_name = input()
my_zoo = Zoo(zoo_name)
num = int(input())

for i in range(num):
    command = input().split(" ")
    species = command[0]
    name = command[1]
    my_zoo.add_animal(species, name)

info = input()
my_tuple = my_zoo.get_info(info)
print(my_tuple[0])
print(my_tuple[1])