class Solution:
    def solve(self, nums):
        for l in range(len(nums),0,-1):
            mn,mx = -inf,inf
            min_pq, max_pq = [], []

            for i in range(l):
                heappush(min_pq,nums[i])
                heappush(max_pq,-1*nums[i])

            removed = set()

            for i in range(l-1,len(nums)):
                while min_pq and min_pq[0] in removed: heappop(min_pq)
                while max_pq and -max_pq[0] in removed: heappop(max_pq)

                mn,mx = min_pq[0], -1*max_pq[0]
                if mx-mn+1 == l: return l

                removed.add(nums[i-l+1])
                if i+1 < len(nums):
                    heappush(min_pq, nums[i+1])
                    heappush(max_pq, -1*nums[i+1])

        return 0
