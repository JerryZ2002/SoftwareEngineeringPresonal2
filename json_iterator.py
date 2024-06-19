# json_iterator.py


class JsonIterator:
    def __init__(self, data):
        self.data = data
        self.keys = list(data.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration
        key = self.keys[self.index]
        value = self.data[key]
        self.index += 1
        return key, value