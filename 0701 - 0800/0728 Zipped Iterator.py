class ZippedIterator:
    def __init__(self, a, b):
        self.vals = sum(map(list,zip(a,b)), []) + a[min(len(a),len(b)):] + b[min(len(a),len(b)):]
        self.i = 0

    def next(self):
        self.i += 1
        return self.vals[self.i-1]

    def hasnext(self):
        return self.i < len(self.vals)
