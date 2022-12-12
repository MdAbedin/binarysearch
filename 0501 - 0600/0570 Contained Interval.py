class Solution:
    def solve(self, intervals):
        intervals.sort()
        ll, lr = -inf,-inf

        for cl,cr in intervals:
            if cl == ll: return True
            if cr <= lr: return True
            ll, lr = cl, cr

        return False
