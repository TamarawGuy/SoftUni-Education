def read_next(*args):
    for item in args:
        for ch in item:
            yield ch