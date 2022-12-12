class Solution:
    def solve(self, stacks):
        if not stacks: return 0

        counts = defaultdict(int)

        for stack in stacks:
            if not stack: return 0

            counts[stack[0]] += 1
            for i in range(1,len(stack)):
                stack[i] += stack[i-1]
                counts[stack[i]] += 1

        return max((key for key in counts if counts[key]==len(stacks)),default=0)
