class Solution:
    def solve(self, s):
        counts = [0]*(len(s)+1)
        for count in Counter(s).values():
            counts[count] += 1
        ans = 0
        for i in reversed(range(1,len(s))):
            ans += max(0,counts[i]-1)
            counts[i-1] += max(0,counts[i]-1)
        return ans
