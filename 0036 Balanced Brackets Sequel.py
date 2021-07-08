class Solution:
    def solve(self, s):
        stack = []

        for i,char in enumerate(s):
            if char in ["(","{","["]:
                stack.append(char)
            else:
                if not stack:
                    return False

                if char == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif char == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                else:
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
        
        return not stack
