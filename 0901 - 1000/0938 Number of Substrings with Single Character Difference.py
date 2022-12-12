class Solution:
    def solve(self, s, t):
        ans = 0

        for i in range(len(s)):
            for j in range(i,len(s)):
                for start in range(len(t)-(j-i)):
                    diffs = 0

                    for x in range(j-i+1):
                        if s[i+x] != t[start+x]: diffs += 1
                        if diffs > 1: break

                    if diffs == 1: ans += 1

        return ans
