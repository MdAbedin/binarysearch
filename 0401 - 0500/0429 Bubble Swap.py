class Solution:
    def solve(self, lst0, lst1):
        ans = 0

        for i in range(len(lst1)):
            j = lst0.index(lst1[i])
            ans += j
            lst0.pop(j)

        return ans
