class Solution:
    def solve(self, citations):
        citations.sort()
        return max((i for i in range(1,len(citations)+1) if citations[-i] >= i),default=0)
