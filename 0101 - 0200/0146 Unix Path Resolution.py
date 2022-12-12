class Solution:
    def solve(self, path):
      ans = []

      for part in path:
        if part == "..":
          if ans: ans.pop()
        elif part != ".": ans.append(part)

      return ans
