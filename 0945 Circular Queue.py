class CircularQueue:
    def __init__(self, capacity):
        self.data = [0]*capacity
        self.i = 0
        self.items = 0
        self.capacity = capacity

    def enqueue(self, val):
        if self.items == self.capacity:
            return False

        self.items += 1
        self.data[(self.i + self.items - 1)%self.capacity] = val

        return True

    def dequeue(self):
        if self.items == 0:
            return False

        ans = self.data[self.i]
        self.data[self.i] = 0
        self.i += 1
        self.i %= self.capacity
        self.items -= 1

        return True

    def front(self):
        if self.items == 0:
            return -1

        return self.data[self.i]

    def top(self):
        if self.items == 0:
            return -1

        return self.data[(self.i + self.items - 1)%self.capacity]

    def isFull(self):
        return self.items == self.capacity

    def isEmpty(self):
        return self.items == 0
