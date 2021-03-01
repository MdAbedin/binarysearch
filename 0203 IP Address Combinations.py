class Solution:
    def helper(self, s, group):
      if group == 4: return [""] if s == "" else []

      ans = []

      for i in range(min(3, len(s))):
        if int(s[:i+1]) <= 255 and (s[0] != "0" or i==0):
          for suffix in self.helper(s[i+1:], group+1):
            ans.append(s[:i+1] + ("." if group < 3 else "") + suffix)

      return ans

    def solve(self, ip):
        return sorted(self.helper(ip, 0))
