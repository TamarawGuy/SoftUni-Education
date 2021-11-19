from project.hero import Hero


class Elf(Hero):
    def __repr__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"


e = Elf("E", 4)
print(str(e))