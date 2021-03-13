class Solution:
    def solve(self, a, b):
        ans,i,j = 0,0,0
        while i < len(a) and j < len(b):
            count = min(a[i],b[j])
            ans += (a[i+1]*b[j+1])*count
            a[i] -= count
            if a[i] == 0: i += 2
            b[j] -= count
            if b[j] == 0: j += 2
        return ans
