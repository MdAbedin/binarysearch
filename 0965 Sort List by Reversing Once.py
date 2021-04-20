class Solution:
    def solve(self, nums):
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                a = i-1
                while a > 0 and nums[a-1] == nums[a]: a -= 1

                for j in range(i,len(nums)):
                    if j == len(nums)-1 or nums[j] < nums[j+1]:
                        b = j
                        break

                return nums[:a] + nums[a:b+1][::-1] + nums[b+1:] == sorted(nums)

        return True
