class MutableRangeSum:
    def __init__(self, nums):
        self.n = len(nums)
        self.bit = [0]*len(nums)
        
        for i in range(self.n):
          self.add(i, nums[i])

    def total(self, i, j):
        return self.sum(j-1) - self.sum(i-1)
    
    def sum(self, r):
      ans = 0
      
      while r >= 0:
        ans += self.bit[r]
        r = (r & (r+1))-1
      
      return ans
      
    def add(self, idx, d):
      while idx < self.n:
        self.bit[idx]  += d
        idx = idx | (idx+1)
          
    def update(self, idx, val):
        self.add(idx, val-self.total(idx,idx+1))
