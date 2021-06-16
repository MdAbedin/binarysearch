class Solution:
    def solve(self, a, b):
        a.sort(reverse=True)
        b.sort(reverse=True)

        i = 0
        j = 0
        ans = 0

        while i < len(a):
            while j < len(b) and b[j] >= a[i]:
                j += 1

            if j >= len(b):
                break

            ans += 1
            i += 1
            j += 1

        return ans
