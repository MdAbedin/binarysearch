class Solution:
    def solve(self, matrix):
        if not matrix:
            return -1
            
        sets = [set(row) for row in matrix]
        return next((num for num in matrix[0] if all(num in row for row in matrix)), -1)
