class Solution:
    def solve(self, nums):
        sums = sorted([[nums[i]+nums[j],i,j] for i in range(len(nums)) for j in range(i+1,len(nums))])
        ans = inf

        for i,(pair_sum,idx1,idx2) in enumerate(sums):
            l,r = i-1,i+1

            while l >= 0 and (sums[l][1] in [idx1,idx2] or sums[l][2] in [idx1,idx2]): l -= 1
            while r < len(sums) and (sums[r][1] in [idx1,idx2] or sums[r][2] in [idx1,idx2]): r += 1

            if l >= 0: ans = min(ans, abs(pair_sum - sums[l][0]))
            if r < len(sums): ans = min(ans, abs(pair_sum - sums[r][0]))

        return ans
