class Solution:
    def solve(self, rod_lens, profit_per_len, cost_per_cut):
        return max((sum(max(0, profit_per_len * (rod_len//sell_len) * sell_len - max(0, cost_per_cut * ((rod_len-1)//sell_len))) for rod_len in rod_lens) for sell_len in range(1,max(rod_lens, default = 0)+1)), default = 0)
