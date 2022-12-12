class Solution:
    def solve(self, s):
        counts = Counter(s[i:j+1] for i in range(len(s)) for j in range(i,len(s)))
        return max((len(substring) for substring,count in counts.items() if count >= 2), default = 0)
