class Solution:
    def solve(self, nums):
        L = [[0,0]]

        for i in range(len(nums)):
            if i%2 == 0:
                L.append([L[-1][0]+nums[i], L[-1][1]])
            else:
                L.append([L[-1][0], L[-1][1]+nums[i]])

        R = [[0,0]]

        for i in range(len(nums)-1,-1,-1):
            if i%2 == 0:
                R.append([R[-1][0]+nums[i], R[-1][1]])
            else:
                R.append([R[-1][0], R[-1][1]+nums[i]])
        
        R.reverse()

        return sum(L[i][0]+R[i+1][1]==L[i][1]+R[i+1][0] for i in range(len(nums)))
