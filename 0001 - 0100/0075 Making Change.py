class Solution:
    def solve(self, n):
        return n//25 + (n%25)//10 + ((n%25)%10)//5 + (((n%25)%10)%5)//1
