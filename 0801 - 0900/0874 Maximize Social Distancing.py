class Solution:
    def solve(self, seats):
        ldists = []
        last = -inf

        for i in range(len(seats)):
            if seats[i] == 1:
                last = i
                ldists.append(inf)
            else:
                ldists.append(i-last)

        rdists = []
        last = inf

        for i in range(len(seats)-1,-1,-1):
            if seats[i] == 1:
                last = i
                rdists.append(inf)
            else:
                rdists.append(last-i)

        rdists.reverse()

        return max(min(ldists[i],rdists[i]) for i in range(len(seats)) if seats[i] == 0)
