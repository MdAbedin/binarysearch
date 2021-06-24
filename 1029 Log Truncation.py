class Solution:
    def solve(self, logs, limit):
        l,r = 0,min(limit, max(logs))
        ans = 0

        while l <= r:
            mid = (l+r)//2

            if sum(min(x,mid) for x in logs) <= limit:
                ans = mid
                l = mid+1
            else:
                r = mid-1

        return ans
