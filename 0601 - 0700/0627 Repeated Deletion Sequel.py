class Solution:
    def solve(self, s, k):
        stack = [["",1]]
        
        for i in range(len(s)):
            if s[i] == stack[-1][0]:
                stack.append([s[i],stack[-1][1]+1])
            else:
                stack.append([s[i],1])

            if stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
                    
        return "".join(p[0] for p in stack)
