class Solution:
    def solve(self, nums):
        ldist,rdist = 0,sum(i for i in range(1,len(nums)) if nums[i] == 1)
        lcount,rcount = 0,sum(nums[i] for i in range(1,len(nums)))
        ans = []

        for i in range(len(nums)):
            ans.append(ldist + rdist)
            ldist += lcount
            rdist -= rcount

            if nums[i] == 1:
                ldist += 1
                lcount += 1

            if i+1 < len(nums) and nums[i+1] == 1:
                rcount -= 1

        return ans
