class Solution:
    def solve(self, board):
        ans = [[0]*len(board[0]) for i in range(len(board))]
        seen = set()

        for y in range(len(board)):
          bfs = deque()

          for coords in [(y,0), (y,len(board[0])-1)]:
            if coords not in seen and board[coords[0]][coords[1]] == 1:
              seen.add(coords)
              bfs.append(coords)
          
          while bfs:
            cy,cx = bfs.popleft()
            ans[cy][cx] = 1

            for ny,nx in [(cy+1,cx), (cy-1,cx), (cy,cx+1), (cy,cx-1)]:
              if 0<=ny<len(board) and 0<=nx<len(board[0]) and (ny,nx) not in seen and board[ny][nx] == 1:
                seen.add((ny,nx))
                bfs.append((ny,nx))

        for x in range(len(board[0])):
          bfs = deque()

          for coords in [(0,x), (len(board)-1,x)]:
            if coords not in seen and board[coords[0]][coords[1]] == 1:
              seen.add(coords)
              bfs.append(coords)
          
          while bfs:
            cy,cx = bfs.popleft()
            ans[cy][cx] = 1

            for ny,nx in [(cy+1,cx), (cy-1,cx), (cy,cx+1), (cy,cx-1)]:
              if 0<=ny<len(board) and 0<=nx<len(board[0]) and (ny,nx) not in seen and board[ny][nx] == 1:
                seen.add((ny,nx))
                bfs.append((ny,nx))

        return ans
