class Solution:
    def solve(self, exp):
        stack = []

        for element in exp:
            if element in ["+", "-", "*", "/"]:
                right_argument = stack.pop()
                left_argument = stack.pop()
                result = int(eval(left_argument + element + right_argument))
                stack.append(str(result))
            else:
                stack.append(element)

        return int(stack[0])
