class Solution:
    def helper(self, n):
        if n == 0:
            return 0
            
        biggest_under = bisect_left(self.fib, n+1)-1

        return 1 + self.helper(n-self.fib[biggest_under])

    def solve(self, n):
        fib = [0,1]

        while fib[-1] < 2**31:
            fib.append(fib[-1]+fib[-2])

        self.fib = fib

        return self.helper(n)
