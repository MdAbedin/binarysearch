class Solution:
    def solve(self, s):
        s = s.replace('(',' ( ').replace(')',' ) ')
        tokens = s.split()
        stack = []

        for token in tokens:
            if token == 'true':
                if stack and stack[-1] in ['or','and']:
                    if stack[-1] == 'or':
                        stack.pop()
                        stack.append(stack.pop() or True)
                    else:
                        stack.pop()
                        stack.append(stack.pop() and True)
                else:
                    stack.append(True)
            elif token == 'false':
                if stack and stack[-1] in ['or','and']:
                    if stack[-1] == 'or':
                        stack.pop()
                        stack.append(stack.pop() or False)
                    else:
                        stack.pop()
                        stack.append(stack.pop() and False)
                else:
                    stack.append(False)
            elif token == '(':
                stack.append('(')
            elif token == ')':
                val = stack.pop()
                stack.pop()

                if stack and stack[-1] in ['or','and']:
                    if stack[-1] == 'or':
                        stack.pop()
                        stack.append(stack.pop() or val)
                    else:
                        stack.pop()
                        stack.append(stack.pop() and val)
                else:
                    stack.append(val)
            elif token == 'or':
                stack.append('or')
            elif token == 'and':
                stack.append('and')

        return stack[0]
