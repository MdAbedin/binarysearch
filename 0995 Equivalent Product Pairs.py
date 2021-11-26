class Solution:
    def solve(self, nums):
        return sum(8*count*(count-1)//2 for count in Counter(nums[i]*nums[j] for i in range(len(nums)) for j in range(i+1,len(nums))).values())
