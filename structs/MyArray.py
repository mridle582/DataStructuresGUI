class MyArray:

    def __init__(self, max_size):
        self.data = []
        self.max_size = max_size

    def add(self, value):
        if (len(self.data)) < self.max_size:
            self.data.append(value)
        else:
            print('The list is full.')

    def insert(self, index, value):
        if (len(self.data) < self.max_size) and (index <= len(self.data)):
            self.data.insert(index, value)
        else:
            print('The list is either full or index entered is out of bounds.')

    def remove(self, data):
        if len(self.data) > 0:
            self.data.remove(data)
        else:
            print('The list is empty.')
