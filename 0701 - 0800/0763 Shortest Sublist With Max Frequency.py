class Solution:
    def solve(self, nums):
        k = Counter(nums).most_common(1)[0][1]

        locs = defaultdict(list)

        for i in range(len(nums)):
            locs[nums[i]].append(i)

        return min(locs[num][i+k-1]-locs[num][i]+1 for num in locs for i in range(len(locs[num])-k+1))
