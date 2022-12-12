class Solution:
    def solve(self, nums0, nums1, k):
        if not nums0 or not nums1:
            return 0
            
        nums0.sort()
        nums1.sort()
        pq = []

        for i,num in enumerate(nums0):
            heappush(pq, [-(num+nums1[-1]),i,len(nums1)-1])

        ans = []

        while len(ans) < k:
            num,i,j = heappop(pq)
            ans.append(-num)

            if j-1 >= 0:
                heappush(pq,[-(nums0[i]+nums1[j-1]), i, j-1])

        return sum(ans)
