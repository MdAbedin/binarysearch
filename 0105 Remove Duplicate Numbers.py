class Solution:
    def solve(self, nums):
        counts = Counter(nums)
        frontier = 0

        for i,num in enumerate(nums):
            if counts[num] == 1:
                nums[frontier], nums[i] = nums[i], nums[frontier]
                frontier += 1

        while frontier < len(nums):
            nums.pop()

        return nums
