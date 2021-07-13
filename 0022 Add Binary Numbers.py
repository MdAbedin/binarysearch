class Solution:
    def solve(self, a, b):
        s = max(len(a),len(b))
        a = a.rjust(s,"0")
        b = b.rjust(s,"0")
        carry = 0
        ans = []

        for x,y in zip(reversed(a),reversed(b)):
            sum_ = int(x)+int(y)+carry
            ans.append(sum_%2)
            carry = 1 if sum_ >= 2 else 0

        ans.append(carry)
        ans = "".join(map(str,reversed(ans))).lstrip('0')

        return ans if ans else "0"
