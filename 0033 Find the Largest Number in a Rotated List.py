class Solution:
    def solve(self, arr):
        if arr[0] <= arr[-1]: return arr[-1]
        
        l,r = 0, len(arr)-2
        ans = -1

        while l <= r:
          mid = (l+r)//2

          if arr[mid] >= arr[0]:
            ans = mid
            l = mid+1
          else:
            r = mid-1

        return arr[ans]
