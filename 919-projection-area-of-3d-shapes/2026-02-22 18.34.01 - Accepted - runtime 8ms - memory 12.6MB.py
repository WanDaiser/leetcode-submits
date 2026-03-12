class Solution(object):
    def projectionArea(self, grid):
        n=len(grid)
        top,front,side=0,0,0
        for i in range(n):
            row_max=0
            col_max=0
            for j in range(n):
                if grid[i][j]>0:
                    top+=1
                row_max=max(grid[i][j],row_max)
                col_max=max(grid[j][i],col_max)
            front+=row_max
            side+=col_max
        return top + side + front