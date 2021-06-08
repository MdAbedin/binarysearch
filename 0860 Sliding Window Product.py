class SlidingWindowProduct:
    def __init__(self):
        self.prods = [1]
        self.last0 = 1

    def add(self, num):
        if num == 0:
            self.prods.append(self.prods[-1])
            self.last0 = 0
        else:
            self.prods.append(self.prods[-1]*num)
            self.last0 += 1

    def product(self, k):
        if self.last0 <= k-1:
            return 0
        else:
            return self.prods[-1]//self.prods[~k]
