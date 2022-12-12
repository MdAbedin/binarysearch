class Solution:
    def solve(self, n, seats):
        x = 0

        for i in range(len(seats)):
            if seats[i] == 0 and (i == 0 or seats[i-1] == 0) and (i == len(seats)-1 or seats[i+1] == 0):
                x += 1
                seats[i] = 1

        return x >= n
