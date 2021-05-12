class Solution:
    def solve(self, n):
        ans = []

        while n > 0:
            ans.append(chr(ord("A") + (n-1)%26))
            n = (n-1)//26

        ans.reverse()

        return "".join(ans)
