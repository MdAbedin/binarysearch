class Solution:
    def solve(self, nums, ranges):
        counts = [0]*(len(nums)+1)

        for i,j in ranges:
            counts[i] += 1
            counts[j+1] -= 1

        counts = list(accumulate(counts))[:-1]
        rearranged = [0]*len(nums)

        for num, (count, i) in zip(sorted(nums,reverse=True), sorted([[count,i] for i,count in enumerate(counts)], reverse = True)):
            rearranged[i] = num

        psums = list(accumulate([0]+rearranged))
        MOD = 10**9+7

        return sum((psums[j+1]-psums[i])%MOD for i,j in ranges)%MOD
