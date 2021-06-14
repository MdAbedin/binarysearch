class Solution:
    def solve(self, nums):
        if not nums:
            return 0

        l_streaks = [1]

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                l_streaks.append(l_streaks[-1]+1)
            else:
                l_streaks.append(1)

        r_streaks = [1]

        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]:
                r_streaks.append(r_streaks[-1]+1)
            else:
                r_streaks.append(1)

        r_streaks.reverse()

        return max((1+l_streaks[i-1]+r_streaks[i+1] for i in range(1,len(nums)-1) if nums[i-1]<nums[i]>nums[i+1]), default=0)
