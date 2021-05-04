class Solution:
    def solve(self, coordinates):
        if len(coordinates) <= 1:
            return True

        if len(set(coords[0] for coords in coordinates)) == 1:
            return True

        dy = coordinates[1][1] - coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]
        
        for i in range(len(coordinates)-1):
            dy2 = coordinates[i+1][1] - coordinates[i][1]
            dx2 = coordinates[i+1][0] - coordinates[i][0]
            
            if dx2 == 0:
                return False

            if dy*dx2 != dy2*dx:
                return False

        return True
