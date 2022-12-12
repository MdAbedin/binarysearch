class Solution:
    def solve(self, n):
        l,r = 0,n

        while l <= r:
            mid = (l+r)//2
            square = mid**2

            if square == n: return True
            if square < n:
                l = mid + 1
            if square > n:
                r = mid - 1

        return False
