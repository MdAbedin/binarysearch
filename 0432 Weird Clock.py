class Solution:
    def solve(self, s):
        h,m = map(int, s.split(":"))
        digits = set(s)-{":"}

        while True:
            m += 1

            if m == 60:
                m = 0
                h += 1

                if h == 24:
                    h = 0

            if set(str(h).rjust(2,"0") + str(m).rjust(2,"0")).issubset(digits):
                return str(h).rjust(2,"0") + ":" + str(m).rjust(2,"0")
