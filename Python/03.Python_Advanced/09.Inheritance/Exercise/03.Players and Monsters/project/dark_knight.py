from project.knight import Knight


class DarkKnight(Knight):
    def __repr__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"