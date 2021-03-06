class Solution:
    def solve(self, n):
        s = "1"

        for i in range(1,n):
            ans = ""
            c = s[0]
            count = 0

            for char in s:
                if char == c:
                    count += 1
                else:
                    ans += str(count) + str(c)
                    count = 1
                    c = char

            ans += str(count) + str(c)
            s = ans

        return s
