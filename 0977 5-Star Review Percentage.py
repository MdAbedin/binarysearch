class Solution:
    def solve(self, reviews, t):
        if t == 100: return 0
        if t == 0: return 0

        A = sum(review[0] for review in reviews)
        B = sum(review[1] for review in reviews)

        return ceil((t*B-100*A)/(100-t))
