class Solution:
    def solve(self, a, b, lower, upper):
        a = [x**2 for x in a]
        a.sort()
        b = [x**2 for x in b]
        b.sort()
        ans = 0

        for i in range(len(a)):
            l,r = 0,len(b)-1
            ans1 = -1

            while l<=r:
                mid = (l+r)//2

                if a[i] + b[mid] >= lower:
                    ans1 = mid
                    r = mid-1
                else:
                    l = mid+1

            l,r = 0,len(b)-1
            ans2 = -1

            while l<=r:
                mid = (l+r)//2

                if a[i] + b[mid] <= upper:
                    ans2 = mid
                    l = mid+1
                else:
                    r = mid-1

            if -1 in [ans1,ans2]: continue
            ans += ans2-ans1+1

        return ans
