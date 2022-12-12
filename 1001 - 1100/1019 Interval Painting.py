class Solution:
    def solve(self, nums, target):
        points = {0}
        cur = 0
        for num in nums:
            cur += num
            points.add(cur)
        points = sorted(list(points))
        locs = {points[i]:i for i in range(len(points))}
        ans = [0]*(len(points)+1)
        cur = 0
        for num in nums:
            ans[locs[min(cur,cur+num)]] += 1
            ans[locs[max(cur,cur+num)]] -= 1
            cur += num

        for i in range(1,len(ans)):
            ans[i] += ans[i-1]

        # print(ans)
        # print(points)
        return sum(((points[i+1] if i+1<len(points) else points[i]+1)-points[i] if ans[i] >= target else 0) for i in range(len(ans)))
