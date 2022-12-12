class Solution:
    def solve(self, nums, queries):
        pxors = [0]

        for num in nums:
            pxors.append(pxors[-1]^num)

        return [pxors[j+1]^pxors[i] for i,j in queries]
