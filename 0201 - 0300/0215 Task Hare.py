class Solution:
    def solve(self, tasks, people):
        tasks.sort()
        people.sort()
        ans = 0
        i = len(people)-1
        j = len(tasks)-1

        while i >= 0 and j >= 0:
            if people[i] >= tasks[j]:
                ans += 1
                i -= 1
                j -= 1
            else:
                j -= 1

        return ans
