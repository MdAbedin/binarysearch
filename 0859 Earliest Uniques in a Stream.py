class EarliestUnique:
    def __init__(self, nums):
        self.nums_set = set()
        self.uniques = set()
        self.order = deque()

        for num in nums:
             self.add(num)       

    def add(self, num):
        if num in self.nums_set:
            self.uniques.discard(num)
        else:
            self.nums_set.add(num)
            self.uniques.add(num)
            self.order.append(num)

    def earliestUnique(self):
        while self.order and self.order[0] not in self.uniques: self.order.popleft()
        if not self.order: return -1
        return self.order[0]
