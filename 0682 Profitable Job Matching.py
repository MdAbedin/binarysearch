class Solution:
    def solve(self, people, jobs, profits):
        data = [[0,0]]+sorted(map(list,zip(jobs,profits)))

        for i in range(1,len(data)):
            data[i][1] = max(data[i][1], data[i-1][1])

        return sum(data[bisect_right(data, [person, inf])-1][1] for person in people)
