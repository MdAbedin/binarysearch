class Solution:
    def solve(self, n):
        facts = [prod(range(1,i+1)) for i in range(1,13)]

        def solve(n, right_bound):
            if n == 0: return True
            right_bound = min(right_bound, bisect_right(facts,n))
            return any(n - facts[i] >= 0 and solve(n-facts[i], i) for i in range(right_bound-1,-1,-1))

        return solve(n, len(facts))
