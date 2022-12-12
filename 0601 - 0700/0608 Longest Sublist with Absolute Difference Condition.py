class Solution:
    def solve(self, nums, k):
        if not nums or k < 0: return 0

        l,r = 0,0
        min_pq,max_pq = [],[]
        ans = 1

        while r < len(nums):
            while min_pq and min_pq[0][1] < l: heappop(min_pq)
            while max_pq and max_pq[0][1] < l: heappop(max_pq)
            heappush(min_pq, [nums[r], r])
            heappush(max_pq, [-nums[r], r])

            while r+1 < len(nums):
                heappush(min_pq, [nums[r+1],r+1])
                heappush(max_pq, [-nums[r+1],r+1])

                if -max_pq[0][0] - min_pq[0][0] <= k:
                    ans = max(ans, r+1-l+1)
                    r += 1
                else:
                    break

            l += 1
            r += 1

        return ans
