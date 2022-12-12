class Solution:
    def solve(self, s):
        char_locs = [-1]+[i for i in range(len(s)) if s[i].isalpha()]
        ans = []

        for i in range(1,len(char_locs)):
          ans += [s[char_locs[i]]]*int(s[char_locs[i-1]+1:char_locs[i]])

        return "".join(ans)
