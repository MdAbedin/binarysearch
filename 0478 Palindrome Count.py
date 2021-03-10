class Solution:
    def solve(self, s, k):
        if not s: return 1 if k == 0 else 0
        
        s = set(s)
        dp = [len(s)] if k%2 == 1 else [1]

        return (len(s) if k%2 == 1 else 1)**(k//2)
        for i in range(k//2):
            dp.append(dp[-1]*len(s))

        return dp[-1]
