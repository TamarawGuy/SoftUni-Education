class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if self.capacity - ml < 0:
            return f"Cannot add {ml} ml"

        if self.capacity - ml >= 0 and self.content + ml <= Glass.capacity:
            self.capacity -= ml
            self.content += ml
            return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{Glass.capacity - self.content} ml left"