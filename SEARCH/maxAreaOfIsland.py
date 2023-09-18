dirctions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
## dfs
def maxAreaOfIsland(grid):
    if not grid:
        return 0

    maxArea = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            maxArea = max(getMaxArea(grid, x, y), maxArea)
    return maxArea

def getMaxArea(grid, x, y):
    if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == 0:
        return 0
    area = 1
    grid[x][y] = 0
    for d in dirctions:
        dx, dy = d
        area += getMaxArea(grid, x + dx, y + dy)
    return area



### disjoint set union

##       map: 0 1 2 3
##    parent: 0 0 2 2
## size/rank: 2 1 2 1

# two functions: find() => get parent
#                union(a, b) => link 2 sets together and change size/rank
def maxAreaOfIsland_dsu(grid):

    def find(u):
        if u == parent[u]:
            return u
        else:
            ## TODO change the shape of set => deep to low
            parent[u] = find(parent[u])
            return parent[u]
    def union(a, b):
        pa, pb = find(a), find(b)
        if pa == pb:
            return
        if size[pb] > size[pa]:
            parent[pa] = pb
            size[pb] += size[pa]
        else:
            parent[pb] = pa
            size[pa] += size[pb]

    if not grid:
        return 0
    m = len(grid)
    n = len(grid[0])
    f = 0
    parent = [i for i in range(m*n)]
    size = [1 for i in range(m*n)]
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                f = 1
                a = i*n + j
                for u,v in [(i-1,j), (i+1,j), (i, j-1), (i, j+1)]:
                    if 0<=u<m and 0<=v<n and grid[u][v]:
                        b = u*n+v
                        union(a, b)
    if f==0:
        return 0
    return max(size)


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland_dsu(grid))








