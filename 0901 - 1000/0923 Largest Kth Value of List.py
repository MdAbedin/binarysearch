class Solution:
    def solve(self, n, total, k):
        gauss = lambda x,y=0: x*(x+1)//2 - y*(y-1)//2
        
        def works(x):
          return x + gauss(x-1,x-k) + gauss(x-1,x-(n-k-1)) <= total
          
        l,r = 0,max(total,n)
        ans = -1
        
        while l <= r:
          mid = (l+r)//2
          
          if works(mid):
            ans = mid
            l = mid+1
          else:
            r = mid-1
        
        return ans
