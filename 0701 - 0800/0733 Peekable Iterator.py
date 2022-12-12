class PeekableIterator:
    def __init__(self, nums):
        self.nums = nums
        self.i = 0

    def peek(self):
        return self.nums[self.i]

    def next(self):
        self.i += 1
        return self.nums[self.i-1]

    def hasnext(self):
        return self.i < len(self.nums)
        
