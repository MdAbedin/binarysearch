class Solution:
    def solve(self, sx, sy, ex, ey, roads):
        if (sx,sy) == (ex,ey): return 0
        
                
        points = {(sx,sy):1}
        used = 0

        for nx,ny in [[ex+1,ey],[ex-1,ey],[ex,ey+1],[ex,ey-1]]:
                if (nx,ny) in points and points[(nx,ny)] == 1: return used

        for x,y in roads:
            used += 1
            if (x,y) in points: continue
            points[(x,y)] = 0

            for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if (nx,ny) in points and points[(nx,ny)] == 1:
                    points[(x,y)] = 1
                    dfs = [(x,y)]

                    while dfs:
                        cx,cy = dfs.pop()

                        for nx,ny in [[cx+1,cy],[cx-1,cy],[cx,cy+1],[cx,cy-1]]:
                            if (nx,ny) in points and points[(nx,ny)] == 0:
                                points[(nx,ny)] = 1
                                dfs.append((nx,ny))

                    break

            for nx,ny in [[ex+1,ey],[ex-1,ey],[ex,ey+1],[ex,ey-1]]:
                if (nx,ny) in points and points[(nx,ny)] == 1: return used

        return -1
