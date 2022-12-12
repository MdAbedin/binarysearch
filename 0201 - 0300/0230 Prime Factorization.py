class Solution:
    def solve(self, n):
        ans = []

        while n%2 == 0:
            ans.append(2)
            n //= 2

        for i in range(3,floor(sqrt(n))+1,2):
            while n%i == 0:
                ans.append(i)
                n //= i

        if n > 2: ans.append(n)

        return ans
