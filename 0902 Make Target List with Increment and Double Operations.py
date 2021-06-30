class Solution:
    def solve(self, target):
        ans = 0
        max_doubles = 0

        for num in target:
            doubles = 0

            while num:
                if num%2 == 0:
                    num //= 2
                    doubles += 1
                else:
                    num -= 1
                    ans += 1

            max_doubles = max(max_doubles, doubles)

        return ans+max_doubles
