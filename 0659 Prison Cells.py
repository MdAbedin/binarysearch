class Solution:
    def solve(self, nums, k):
        history = [nums[:]]
        seen = {tuple(nums)}
        before_cycle = []
        cycle = []

        while True:
            nums2 = [0]*8

            for i in range(1,7):
                l = (nums[i-1] if i-1 >= 0 else 0) + (nums[i+1] if i+1 < 8 else 0)
                nums2[i] = 1 - l%2

            nums = nums2
            
            if tuple(nums) in seen:
                i = history.index(nums)
                before_cycle = history[:i]
                cycle = history[i:]
                break
            
            history.append(nums[:])
            seen.add(tuple(nums))

        return before_cycle[k] if k < len(before_cycle) else cycle[(k-len(before_cycle))%len(cycle)]
