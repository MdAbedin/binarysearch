class Solution:
    def solve(self, coordinates):
        remove = set()
        coordinates = list(zip(coordinates,range(len(coordinates))))
        coordinates.sort()

        max_y = -inf
        for i in range(len(coordinates)-1,-1,-1):
            cur_y = coordinates[i][0][1]
            if max_y >= cur_y: remove.add(coordinates[i][1])
            max_y = max(max_y, cur_y)

        coordinates.sort(key = lambda x: x[0][::-1])
        
        max_x = -inf
        
        for i in range(len(coordinates)-1,-1,-1):
            cur_x = coordinates[i][0][0]
            if max_x >= cur_x: remove.add(coordinates[i][1])
            max_x = max(max_x, cur_x)

        coordinates.sort(key = lambda x: x[1])

        return [coordinates[i][0] for i in range(len(coordinates)) if i not in remove]
