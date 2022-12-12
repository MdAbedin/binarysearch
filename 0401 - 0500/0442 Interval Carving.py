class Solution:
    def solve(self, intervals, cut):
        ans = []

        for i in range(len(intervals)):
            if cut[0] >= intervals[i][1]:
                ans.append(intervals[i])
            elif cut[0] > intervals[i][0]:
                ans.append([intervals[i][0], cut[0]])
                if cut[1] < intervals[i][1]:
                    ans.append([cut[1], intervals[i][1]])
            elif cut[1] > intervals[i][0]:
                if cut[1] < intervals[i][1]:
                    ans.append([cut[1], intervals[i][1]])
            else:
                ans.append(intervals[i])

        return ans
