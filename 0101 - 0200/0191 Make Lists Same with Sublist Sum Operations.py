class Solution:
    def solve(self, l0, l1):
        if not l0 or not l1: return 0 if not l0 and not l1 else -1
        l0 = list(accumulate(l0))
        l1 = list(accumulate(l1))
        ans = 0

        for i in range(len(l0)):
            j = bisect_left(l1,l0[i])
            
            if 0<=j<len(l1) and l1[j] == l0[i]:
                ans += 1
                if i == len(l0)-1 and j != len(l1)-1: return -1
            else:
                if i == len(l0)-1: return -1

        return ans
