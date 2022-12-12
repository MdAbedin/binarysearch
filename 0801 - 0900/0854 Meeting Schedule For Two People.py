class Solution:
    def solve(self, a, b, duration):
        a.sort()
        b.sort()

        starts = {x[0] for x in a} | {x[0] for x in b}
        ans = -1

        for s in starts:
            i = bisect_left(a, [s+1,-1])-1
            j = bisect_left(b, [s+1,-1])-1

            if i != -1 and j != -1:
                s2 = max(a[i][0],b[j][0])

                if a[i][1]-s2 >= duration and b[j][1]-s2 >= duration:
                    return [s2,s2+duration]

        return []
