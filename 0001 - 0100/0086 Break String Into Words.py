class Solution:
    @cache
    def helper(self,i):
      if i == len(self.s): return True

      for j in range(i,len(self.s)):
        if self.s[i:j+1] in self.words and self.helper(j+1): return True

      return False

    def solve(self, words, s):
        self.words = set(words)
        self.s = s
        return self.helper(0)
