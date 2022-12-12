class Solution:
    def solve(self, nums):
        if len(nums) <= 2: return 0

        l_maxes = []
        l_max = -inf

        for num in nums:
            l_max = max(l_max,num)
            l_maxes.append(l_max)

        r_maxes = []
        r_max = -inf

        for num in nums[::-1]:
            r_max = max(r_max,num)
            r_maxes.append(r_max)

        r_maxes.reverse()

        return sum(max(0,min(l_maxes[i-1],r_maxes[i+1])-nums[i]) for i in range(1,len(nums)-1))
