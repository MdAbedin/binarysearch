class Solution:
    def solve(self, n, k):
        ans = []

        for i in range(k):
            ans.append(x := max(1,n-26*(k-i-1)))
            n -= x

        return "".join(chr(ord('a')+x-1) for x in ans)
