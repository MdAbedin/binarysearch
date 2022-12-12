class TwoSum:
    def __init__(self):
        self.counts = dict()

    def add(self, val):
        if val not in self.counts: self.counts[val] = 0
        self.counts[val] += 1

    def find(self, val):
        for key in self.counts:
            if key == val-key:
                if self.counts[key] >= 2:
                    return True
            elif val-key in self.counts:
                return True

        return False
