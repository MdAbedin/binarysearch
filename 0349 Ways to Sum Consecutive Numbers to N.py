class Solution:
    def solve(self, n):
        return 1 if n == 0 else sum((x := (n - k*(k-1)//2)/k) == int(x) and x > 0 for k in range(1,ceil(sqrt(n*2))+3))
