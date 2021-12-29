class Solution:
    def solve(self, a, b):
        negative_coefficient = 1
        if a[0] == "-":
            negative_coefficient *= -1
            a = a[1:]
        if b[0] == "-":
            negative_coefficient *= -1
            b = b[1:]
            
        if len(b) > len(a): a,b = b,a
        a,b = a[::-1], b[::-1]
        ans = [0]*(len(a) + len(b))

        for i in range(len(b)):
            add = [0]*(len(a) + len(b))
            carry = 0

            for j in range(len(a)):
                result = int(a[j]) * int(b[i]) + carry
                carry = result // 10
                add[i+j] = result % 10

            add[i + len(a)] = carry
            carry = 0

            for i in range(len(add)):
                result = ans[i] + add[i] + carry
                carry = result // 10
                ans[i] = result % 10

        while ans[-1] == 0: ans.pop()
        if negative_coefficient == -1: ans.append("-")

        return "".join(map(str, ans))[::-1]
