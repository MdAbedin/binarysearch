class MinimumStack:
    def __init__(self):
        self.stack = [(inf,inf)]

    def append(self, val):
      self.stack.append((val, min(val, self.stack[-1][1])))

    def peek(self):
      return self.stack[-1][0]

    def min(self):
      return self.stack[-1][1]        

    def pop(self):
        return self.stack.pop()[0]
