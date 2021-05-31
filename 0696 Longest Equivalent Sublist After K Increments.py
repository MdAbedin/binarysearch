class Solution:
    def solve(self, nums, k):
        if not nums:
            return 0

        ans = 1
        cur_sum = 0
        maxes = []
        j = -1

        for i in range(len(nums)):
            while maxes and maxes[0][1] < i:
                heappop(maxes)

            if j < i:
                heappush(maxes, [-nums[i],i])

            while j < len(nums)-1 and max(-maxes[0][0], nums[j+1])*(j+1-i+1)-(cur_sum+nums[j+1]) <= k:
                cur_sum += nums[j+1]
                heappush(maxes, [-nums[j+1],j+1])
                j += 1

            ans = max(ans, j-i+1)
            cur_sum -= nums[i]

        return ans
