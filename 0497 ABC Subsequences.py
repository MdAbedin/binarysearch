class Solution:
    def solve(self, s):
        As = [0]

        for i,char in enumerate(s):
            As.append(As[-1] + (1 if char == "a" else 0))

        As = As[1:]
        Cs = [0]

        for i,char in enumerate(s[::-1]):
            Cs.append(Cs[-1] + (1 if char == "c" else 0))

        Cs.reverse()
        Cs = Cs[:-1]

        B_locs = list(filter(lambda x: s[x] == "b", range(len(s))))
        ans = 0
        coeff = 0

        for i in range(len(B_locs)):
            ans += (2**As[B_locs[i]] - 1) * (2**Cs[B_locs[i]] - 1)
            
            ans += coeff * (2**Cs[B_locs[i]] - 1)
            coeff *= 2
            coeff += 2**As[B_locs[i]] - 1

        return ans
