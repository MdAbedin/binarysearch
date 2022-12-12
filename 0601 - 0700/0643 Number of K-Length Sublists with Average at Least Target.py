class Solution:
    def solve(self, nums, k, target):
        psums = [0]

        for num in nums:
            psums.append(psums[-1]+num)

        return sum((psums[i]-psums[i-k]) >= target*k for i in range(k,len(psums)))
