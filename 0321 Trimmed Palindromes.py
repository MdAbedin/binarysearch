class Solution:
    def solve(self, s):
        return [s := "".join(sum([[c,"$"] for c in s], [])),sum((next(j for j in range(len(s)+1) if i+j == len(s) or i-j == -1 or s[i+j] != s[i-j])-1 - i%2)//2+1 for i in range(len(s)))][1]
