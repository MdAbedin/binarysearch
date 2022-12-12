class Solution:
    def solve(self, intervals):
        intervals.sort()
        merged = [intervals[0]]
        ans = -1

        for a,b in intervals:
          if a <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
          else:
            merged.append([a,b])

          ans = max(ans, merged[-1][1]-merged[-1][0]+1)

        return ans
