class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.my_str = ""
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.index
        if len(self.my_str) >= self.number:
            raise StopIteration

        if value >= len(self.sequence):
            value = 0
            self.index = 0

        self.index += 1
        self.my_str += self.sequence[value]
        return self.sequence[value]