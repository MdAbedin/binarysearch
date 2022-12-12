class Solution:
    def solve(self, intervals):
        intervals.sort()
        ans = [intervals[0][:]]

        for a,b in intervals:
          if a > ans[-1][1]: ans.append([a,b])
          else: ans[-1][1] = max(ans[-1][1], b)

        return ans
