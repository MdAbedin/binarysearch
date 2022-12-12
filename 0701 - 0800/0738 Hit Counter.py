class HitCounter:
    def __init__(self):
        self.queue = deque()

    def add(self, timestamp):
        self.queue.append(timestamp)

    def count(self, timestamp):
        while self.queue and self.queue[0] < timestamp-60: self.queue.popleft();return len(self.queue)
