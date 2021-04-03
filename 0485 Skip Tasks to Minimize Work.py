class Solution:
    def solve(self, nums):
        did,didnt = 0,0

        for i in range(len(nums)):
            did,didnt = didnt, nums[i] + min(did,didnt)

        return min(did,didnt)
