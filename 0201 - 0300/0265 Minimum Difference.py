class Solution:
    def solve(self, lst0, lst1):
        lst0.sort()
        lst1.sort()
        i = 0
        ans = inf

        for num in lst0:
            while i+1 < len(lst1) and abs(num - lst1[i+1]) <= abs(num - lst1[i]):
                i += 1

            ans = min(ans, abs(num - lst1[i]))

        return ans
