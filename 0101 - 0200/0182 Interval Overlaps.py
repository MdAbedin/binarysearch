class Solution:
    def solve(self, l0, l1):
        i,j = 0,0
        ans = []

        while i < len(l0) and j < len(l1):
            start,end = max(l0[i][0], l1[j][0]), min(l0[i][1], l1[j][1])

            if start <= end: ans.append([start,end])

            if l0[i][1] < l1[j][1]: i += 1
            else: j += 1

        return ans
