class Solution:
    def solve(self, n):
        return sum((2**i)*((n+1)//2**(i+1)) + max(0,((n+1) - (2**(i+1))*((n+1)//2**(i+1)) - 2**i)) for i in range(ceil(log(n,2))+1))
