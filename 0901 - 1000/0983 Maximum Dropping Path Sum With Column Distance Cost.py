class Solution:
    def solve(self, matrix):
        lpq,rpq = [],[]
        
        for i in range(len(matrix[0])):
          heappush(rpq, [-1*(matrix[0][i]-i), i])

        for y in range(1,len(matrix)):
          # print(rpq)
          new_rpq = []

          for x in range(len(matrix[0])):
            while rpq[0][1] < x:
              v,i = heappop(rpq)
              heappush(lpq, [-1*(-v+2*i), i])

            if lpq:
              vl, il = lpq[0]
              vr, ir = rpq[0]
              vl = -1*(-vl - il - (x-il))
              vr = -1*(-vr + ir - (ir-x))

              heappush(new_rpq, [min(vr,vl)+x-matrix[y][x], x])
            else:
              v,i = rpq[0]
              heappush(new_rpq, [-1*(-v + i - (i-x))+x-matrix[y][x], x])

          lpq,rpq = [], new_rpq

        # print(rpq)
        return max(-a+b for a,b in rpq)
