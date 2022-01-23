class Solution:
    def solve(self, n, k):
        if n == 0: return ""
        p = 3 * (2**(n-1))
        if k not in range(0, p): return ""

        ans = []

        if k < p//3:
            ans.append("0")
        elif k < 2*p//3:
            ans.append("1")
            k -= p//3
        else:
            ans.append("2")
            k -= 2*p//3
        
        p //= 3

        for _ in range(n-1):
            if k < p//2:
                ans.append(min(x for x in "012" if x != ans[-1]))
            else:
                ans.append(max(x for x in "012" if x != ans[-1]))
                k -= p//2

            p //= 2

        return "".join(ans)
