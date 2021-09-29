class Solution:
    def solve(self, nums, target):
        counts = Counter(nums)

        for i in range(len(nums)):
            counts[nums[i]] -= 1
            for j in range(i+1,len(nums)):
                counts[nums[j]] -= 1
                for k in range(j+1,len(nums)):
                    counts[nums[k]] -= 1
                    if counts[target-nums[i]-nums[j]-nums[k]] > 0: return True
                    counts[nums[k]] += 1
                counts[nums[j]] += 1
            counts[nums[i]] += 1

        return False
