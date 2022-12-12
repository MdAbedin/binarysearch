class TwoDimensionalIterator:
    def __init__(self, lists):
        self.vals = sum(lists, [])
        self.i = 0

    def next(self):
        self.i += 1
        return self.vals[self.i-1]

    def hasnext(self):
        return self.i < len(self.vals)
