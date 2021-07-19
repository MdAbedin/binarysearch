class Solution:
    def solve(self, nums, k):
        nums.insert(0,0)
        counts = defaultdict(int, {0:1})
        ans = 0
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            m = nums[i]%k
            ans += counts[m]
            counts[m] += 1

        return ans
