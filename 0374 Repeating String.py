class Solution:
    def solve(self, s):
        if not s: return False

        for i in range(2,len(s)+1):
          if len(s)%i != 0: continue
          works = True
          first = s[:len(s)//i]
          
          for j in range(0,len(s),len(s)//i):
            if s[j:j+len(s)//i] != first:
              works = False
              break

          if works: return True

        return False
