class Solution:
    def solve(self, nums):
        nums_sorted = sorted(nums)
        sorted_locs = {nums_sorted[i]:i for i in range(len(nums_sorted))}
        orig_locs = {nums[i]:i for i in range(len(nums))}
        done = set()
        ans = 0

        for i in range(len(nums)):
            if i in done: continue
            
            j = i

            while j != sorted_locs[nums[i]]:
                done.add(orig_locs[nums_sorted[j]])
                j = orig_locs[nums_sorted[j]]
                ans += 1

            done.add(i)

        return ans
