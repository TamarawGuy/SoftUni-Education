class dictionary_iter:
    def __init__(self, dictionary_obj):
        self.dictionary_obj = dictionary_obj
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.dictionary_obj):
            raise StopIteration

        value = self.index
        self.index += 1
        return f"({self.dictionary_obj[value]}, '{value}')"