class Solution:
    def solve(self, n):
        squares = [num**2 for num in range(1,ceil(sqrt(n))+1)]
        squares_set = set(squares)

        @lru_cache(maxsize=None)
        def helper(x):
            if x == 0: return 0
            if x in squares_set: return 1
            
            ans = inf

            for i in range(bisect_left(squares,x)):
                ans = min(ans, helper(x - squares[i]) + 1)

            return ans
            
        return helper(n)
