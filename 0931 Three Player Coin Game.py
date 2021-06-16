class Solution:
    def solve(self, piles):
        piles.sort(reverse=True)
        return sum(piles[1+i*2] for i in range(len(piles)//3))
