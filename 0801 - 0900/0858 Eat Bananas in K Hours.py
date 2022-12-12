class Solution:
    def works(self,mid,piles,k):
        return sum(ceil(pile/mid) for pile in piles) <= k

    def solve(self, piles, k):
        l,r = 1,max(piles)
        ans = -1

        while l<=r:
            mid = (l+r)//2

            if self.works(mid,piles,k):
                ans = mid
                r = mid-1
            else:
                l = mid+1

        return ans
