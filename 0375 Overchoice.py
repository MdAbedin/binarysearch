class Solution:
    def solve(self, s):
        s = s.replace("[]", "")
        choices = []
        i = 0
        choice_i = 0
        in_brackets = False
        c = []

        while i < len(s):
            if s[i] == "[":
                in_brackets = True
                choices.append([])
            elif s[i] == "|":
                if c:
                    choices[choice_i].append("".join(c))
                    c = []
            elif s[i] == "]":
                if c:
                    choices[choice_i].append("".join(c))
                    c = []
                in_brackets = False
                choice_i += 1
            else:
                if in_brackets:
                    c.append(s[i])
                else:
                    choices.append([s[i]])
                    choice_i += 1

            i += 1

        chars = len(choices)
        dfs = [[]]
        ans = []

        while dfs:
            cur = dfs.pop()

            if len(cur) == chars:
                ans.append("".join(cur))
                continue

            for choice in choices[len(cur)]:
                dfs.append(cur[:]+[choice])

        return ans
