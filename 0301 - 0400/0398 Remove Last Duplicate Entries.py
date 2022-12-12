class Solution:
    def solve(self, nums):
        locs = defaultdict(list)
        
        for i in range(len(nums)):
            locs[nums[i]].append(i)

        return [nums[i] for i in range(len(nums)) if not(len(locs[nums[i]])>1 and i == locs[nums[i]][-1])]
