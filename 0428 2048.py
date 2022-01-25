class Solution:
    def solve(self, board, direction):
        def rotate_cw(matrix): return list(list(col)[::-1] for col in zip(*matrix))
        
        rotations = {
            "left": 0,
            "down": 1,
            "right": 2,
            "up": 3,
        }

        for _ in range(rotations[direction]): board = rotate_cw(board)

        new_board = []

        for row in board:
            new_row = [[None,False]]

            for val in row:
                if val == 0: continue
                if not new_row[-1][1]: new_row.append([val,True])
                elif new_row[-1][0] == val:
                    new_row[-1][0] *= 2
                    new_row[-1][1] = False
                else: new_row.append([val,True])

            new_row = new_row[1:]
            for _ in range(4 - len(new_row)): new_row.append([0,False])
            new_board.append([pair[0] for pair in new_row])

        board = new_board
        for _ in range(4-rotations[direction]): board = rotate_cw(board)

        return board
