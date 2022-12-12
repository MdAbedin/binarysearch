class Solution:
    def solve(self, matrix):
        seen = set()
        borders1, borders2 = [], []
        is_island1 = True

        for y in range(len(matrix)):
          for x in range(len(matrix[0])):
            if (y,x) not in seen and matrix[y][x] == 1:
              seen.add((y,x))
              bfs = deque([(y,x)])

              while bfs:
                cy,cx = bfs.popleft()
                empty_neighbors = 0

                for ny,nx in [(cy+1,cx), (cy-1,cx), (cy,cx+1), (cy,cx-1)]:
                  if 0<=ny<len(matrix) and 0<=nx<len(matrix[0]) and matrix[ny][nx] == 0: empty_neighbors += 1
                  if 0<=ny<len(matrix) and 0<=nx<len(matrix[0]) and (ny,nx) not in seen and matrix[ny][nx] == 1:
                    seen.add((ny,nx))
                    bfs.append((ny,nx))

                if empty_neighbors:
                  if is_island1: borders1.append((cy,cx))
                  else: borders2.append((cy,cx))

              is_island1 = False

        ans = inf

        for y1,x1 in borders1:
          for y2,x2 in borders2:
            ans = min(ans, abs(y2-y1)+abs(x2-x1)-1)

        return ans
