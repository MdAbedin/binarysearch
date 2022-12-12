class Solution:
    def solve(self, matrix):
        dp = [[[0,0,0] for j in range(len(matrix[0]))] for i in range(len(matrix))]
        if 0 not in matrix[-1]: return 0
        for i in range(len(matrix[0])):
            if matrix[-1][i] == 0: dp[-1][i] = [1,1,0]


        for r in range(len(matrix)-1,-1,-1):
            if matrix[r][0] == 0:
                if r != len(matrix)-1 and max(dp[r+1][0]) > 0: dp[r][0][2] = max(dp[r+1][0])+1

            for c in range(1,len(matrix[0])):
                if matrix[r][c] == 0:
                    if max(dp[r][c-1]) > 0: dp[r][c][0] = max(dp[r][c-1][0],dp[r][c-1][2]) + 1
                    if r != len(matrix)-1 and max(dp[r+1][c]) > 0: dp[r][c][2] = max(dp[r+1][c])+1
            
            if matrix[r][-1] == 0:
                if r != len(matrix)-1 and max(dp[r+1][-1]) > 0: dp[r][-1][2] = max(dp[r+1][-1])+1

            for c in range(len(matrix[0])-2,-1,-1):
                if matrix[r][c] == 0:
                    if max(dp[r][c+1]) > 0: dp[r][c][1] = max(dp[r][c+1][1],dp[r][c+1][2]) + 1
                    if r != len(matrix)-1 and max(dp[r+1][c]) > 0: dp[r][c][2] = max(dp[r+1][c])+1

        # for row in dp:
        #     print(row)
        return max(max(l) for l in dp[0])
