class Solution:
    def solve(self, nums, k):
        max_pq = []
        min_pq = []
        ans = float("inf")
        
        for i in range(len(nums)):
          n = nums[i]
          heappush(max_pq,[-1*n,i])
          heappush(min_pq, [n,i])
        
        for i in range(len(nums)-k+1):
          popped_max = []
          popped_min = []
          
          while i <= max_pq[0][1] < i+k:
            popped_max.append(heappop(max_pq))
          
          while i <= min_pq[0][1] < i+k:
            popped_min.append(heappop(min_pq))
            
          ans = min(ans, max_pq[0][0]*-1 - min_pq[0][0])
          
          for p in popped_max:
            heappush(max_pq, p)
          for p in popped_min:
            heappush(min_pq, p)
          
        return ans
