class Solution:
    def solve(self, ratings):
        ans = [1]*len(ratings)

        valley = 0
        for i in range(1,len(ratings)):
            if ratings[i] <= ratings[i-1]:
                valley = i
            else:
                ans[i] = max(ans[i], i-valley+1)

        valley = len(ratings)-1
        for i in reversed(range(len(ratings)-1)):
            if ratings[i] <= ratings[i+1]:
                valley = i
            else:
                ans[i] = max(ans[i], valley-i+1)

        return sum(ans)
