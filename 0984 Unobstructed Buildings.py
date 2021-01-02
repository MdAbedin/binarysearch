class Solution:
    def solve(self, heights):
        mx = -inf
        ans = []
        for i in range(len(heights)-1,-1,-1):
          if mx < heights[i]: ans.append(i)
          mx = max(mx,heights[i])
        return ans[::-1]
