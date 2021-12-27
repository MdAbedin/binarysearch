class Solution:
    def solve(self, n):
        digits = list(str(n))
        ans = n

        for i1,i2 in combinations(range(len(digits)),2):
            new_num = copy.copy(digits)
            new_num[i1],new_num[i2] = new_num[i2],new_num[i1]

            ans = max(ans, int("".join(new_num)))

        return ans
