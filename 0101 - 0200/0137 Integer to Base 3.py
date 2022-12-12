class Solution:
    def solve(self, n):
        if n == 0: return "0"

        ans = []
        
        while n:
            ans.append(str(n%3))
            n //= 3

        return "".join(reversed(ans))
