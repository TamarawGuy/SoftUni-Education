from project.hero import Hero


class Wizard(Hero):
    def __repr__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"