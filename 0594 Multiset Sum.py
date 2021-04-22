class Solution:
    def helper(self, k, i):
        if k <= 0 or i == len(self.nums): return 1 if k == 0 else 0
        return sum(self.helper(k-num,i+1) for num in range(0,k+1,self.nums[i]))

    def solve(self, nums, k):
        if not nums: return 0
        self.nums = sorted(list(set(nums)))
        return self.helper(k,0)
