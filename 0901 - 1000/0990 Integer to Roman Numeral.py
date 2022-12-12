class Solution:
    def solve(self, n):
        ans = []
        n = str(n).rjust(4,"0")

        ans.append("M"*int(n[0]))

        if n[1] == "9":
            ans.append("CM")
        elif n[1] == "4":
            ans.append("CD")
        elif n[1] >= "5":
            ans.append("D")
            ans.append("C"*(int(n[1])-5))
        else:
            ans.append("C"*int(n[1]))

        if n[2] == "9":
            ans.append("XC")
        elif n[2] == "4":
            ans.append("XL")
        elif n[2] >= "5":
            ans.append("L")
            ans.append("X"*(int(n[2])-5))
        else:
            ans.append("X"*int(n[2]))

        if n[3] == "9":
            ans.append("IX")
        elif n[3] == "4":
            ans.append("IV")
        elif n[3] >= "5":
            ans.append("V")
            ans.append("I"*(int(n[3])-5))
        else:
            ans.append("I"*int(n[3]))

        return "".join(ans)
