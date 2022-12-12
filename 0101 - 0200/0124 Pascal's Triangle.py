class Solution:
    def solve(self, n):
        ans = [1]

        for i in range(n):
            ans.append(ans[-1]*(n-i)//(i+1))

        return ans
