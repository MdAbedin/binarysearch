class Solution:
    def solve(self, nums, k):
        min_lens = []
        psum_locs = defaultdict(list,{0:[-1]})
        psum = 0
        ans = inf

        for i in range(len(nums)):
            psum += nums[i]
            new_min_len = inf if not min_lens or min_lens[-1] == -1 else min_lens[-1]

            for loc in psum_locs[psum-k]:
                sub_len = i-loc
                new_min_len = min(new_min_len,sub_len)
                if loc >= 0 and min_lens[loc] != -1: ans = min(ans, sub_len + min_lens[loc])

            min_lens.append(-1 if new_min_len == inf else new_min_len)
            psum_locs[psum].append(i)

        return -1 if ans == inf else ans
