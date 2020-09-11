class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None]*capacity
        self.current = 0

    def append(self, item):

        self.data[self.current] = item

        self.current += 1
        if self.current == self.capacity:
            self.current = 0


    def get(self):
        a = [i for i in self.data if i is not None]

        return a