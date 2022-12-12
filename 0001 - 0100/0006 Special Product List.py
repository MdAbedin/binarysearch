class Solution:
    def solve(self, nums):
        lefts = [1]

        for i in range(len(nums)):
            lefts.append(lefts[-1]*nums[i])

        rights = [1]

        for i in range(len(nums)-1,-1,-1):
            rights.append(rights[-1]*nums[i])

        rights.reverse()

        return [lefts[i]*rights[i+1] for i in range(len(nums))]
