class StockSpan:
    def __init__(self):
        self.stack = [[inf,0]]
        self.adds = 0

    def next(self, price):
        while self.stack[-1][0] <= price: self.stack.pop()
        
        self.adds += 1
        ans = self.adds - self.stack[-1][1]
        
        self.stack.append([price,self.adds])

        return ans
