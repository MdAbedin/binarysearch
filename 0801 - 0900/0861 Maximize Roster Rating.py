class Solution:
    def solve(self, ratings, ages):
        data = sorted(list(map(list,zip(ages,ratings,ratings))))

        for i in range(1,len(data)):
            data[i][2] += max((data[j][2] for j in range(i) if data[j][1] <= data[i][1]), default=0)

        return max(x[2] for x in data)
