class Solution:
    def solve(self, s):
        stack = []
        i = 0

        while i < len(s):
          if s[i:i+2] == "<-":
            if stack: stack.pop()
            i += 2
          else:
            stack.append(s[i])
            i += 1

        return "".join(stack)
