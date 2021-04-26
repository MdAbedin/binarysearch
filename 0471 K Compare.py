class Solution:
    def solve(self, a, b, k):
        if k == 0: return len(a)
        if not b: return 0
        
        b.sort()
        
        return sum(x < b[-k] for x in a)
