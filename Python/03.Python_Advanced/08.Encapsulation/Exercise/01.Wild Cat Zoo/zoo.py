class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        if self.__animal_capacity > 0 and self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > 0:
            self.__workers_capacity -= 1
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"

        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        if worker_name not in [w.name for w in self.workers]:
            return f"There is no {worker_name} in the zoo"
        worker = [w for w in self.workers if w.name == worker_name][0]
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = [w.salary for w in self.workers]
        if self.__budget < sum(salaries):
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= sum(salaries)
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        summation = sum([a.get_needs() for a in self.animals])
        if self.__budget < summation:
            return f"You have no budget to tend the animals. They are happy."

        self.__budget -= summation
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def animals_status(self):
        lion_objects = [l for l in self.animals if type(l).__name__ == "Lion"]
        tiger_objects = [t for t in self.animals if type(t).__name__ == 'Tiger']
        cheetah_objects = [c for c in self.animals if type(c).__name__ == 'Cheetah']

        result = f'You have {len(self.animals)} animals\n'
        result += f"----- {len(lion_objects)} Lions:\n"
        for l in lion_objects:
            result += repr(l) + '\n'
        result += f"----- {len(tiger_objects)} Tigers:\n"
        for t in tiger_objects:
            result += repr(t) + '\n'
        result += f"----- {len(cheetah_objects)} Cheetahs:\n"
        for c in cheetah_objects:
            result += repr(c) + '\n'

        return result[:-1]

    def workers_status(self):
        keeper_objects = [k for k in self.workers if type(k).__name__ == 'Keeper']
        caretaker_objects = [c for c in self.workers if type(c).__name__ == 'Caretaker']
        vet_objects = [v for v in self.workers if type(v).__name__ == 'Vet']

        result = f'You have {len(self.workers)} workers\n'
        result += f"----- {len(keeper_objects)} Keepers:\n"
        for k in keeper_objects:
            result += repr(k) + '\n'
        result += f"----- {len(caretaker_objects)} Caretakers:\n"
        for c in caretaker_objects:
            result += repr(c) + '\n'
        result += f"----- {len(vet_objects)} Vets:\n"
        for v in vet_objects:
            result += repr(v) + '\n'

        return result