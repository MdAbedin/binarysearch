class Solution:
    def solve(self, ribbons, k):
        ribbons.sort()
        l,r = 1,ribbons[-1]
        ans = -1

        while l<=r:
            mid = (l+r)//2

            if sum(ribbon//mid for ribbon in ribbons) >= k:
                ans = mid
                l = mid+1
            else:
                r = mid-1

        return ans
