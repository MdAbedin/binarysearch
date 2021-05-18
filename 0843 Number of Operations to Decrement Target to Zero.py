class Solution:
    def solve(self, nums, target):
        if not nums:
            return 0 if target == 0 else -1

        L = [0]
        
        for i in range(len(nums)):
            L.append(L[-1]+nums[i])

        R = [0]

        for i in range(len(nums)-1,-1,-1):
            R.append(R[-1]+nums[i])

        R.reverse()

        j = 0
        ans = inf
        nums = [0]+nums

        for i in range(len(L)):
            while j < len(R) and L[i]+R[j] > target:
                j += 1

            if j >= len(R) or j < i:
                break

            if L[i]+R[j] == target:
                ans = min(ans, i+len(R)-1-j)
        
        return -1 if ans==inf else ans
