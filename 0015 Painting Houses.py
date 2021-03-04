class Solution:
    def solve(self, matrix):
        if not matrix or not matrix[0]: return 0

        min1,min2 = 0,0
        min_i = -1

        for row in matrix:
          new_min1,new_min2 = inf,inf
          new_min_i = -1

          for i,cost in enumerate(row):
            new_cost = cost + (min2 if i == min_i else min1)

            if new_cost < new_min1:
              new_min2 = new_min1
              new_min1 = new_cost
              new_min_i = i
            elif new_cost < new_min2:
              new_min2 = new_cost

          min1,min2,min_i = new_min1,new_min2,new_min_i

        return min1
