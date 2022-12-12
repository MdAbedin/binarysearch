class Solution:
    def solve(self, typed, target):
        if not typed or not target: return typed == target == ""
        if typed[0] != target[0]: return False

        i,j = 1,1

        while i < len(typed) and j < len(target):
            if typed[i] == target[j]:
                i += 1
                j += 1
            else:
                if typed[i] == typed[i-1]: i += 1
                else: return False

        return j == len(target) and len(set(typed[i-1:])) == 1
