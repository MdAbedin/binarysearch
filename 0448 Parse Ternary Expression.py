class Solution:
    def solve(self, s):
        colons = dict()
        tokens = s.split()
        questions = dict()
        level = 0

        for i in range(len(tokens)):
            if tokens[i] == "?":
                level += 1
                questions[level] = i
            elif tokens[i] == ":":
                colons[questions[level]] = i
                level -= 1

        cur = 0

        while cur != len(tokens)-1 and tokens[cur+1] == "?":
            if tokens[cur] == "true":
                cur += 2
            else:
                cur = colons[cur+1]+1

        return tokens[cur] == "true"
