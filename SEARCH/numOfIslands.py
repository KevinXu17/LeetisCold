## TODO disjoin set union
def numIslands(grid):
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
        parent[pb] = pa
        size[pa] = 1
        size[pb] = 0

    if not grid:
        return 0
    m = len(grid)
    n = len(grid[0])
    f = 0
    parent = [i for i in range(m * n)]
    size = [0] * (m*n)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                size[i * n + j] = 1
            else:
                size[i * n + j] = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                f = 1
                a = i * n + j
                for u, v in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= u < m and 0 <= v < n and grid[u][v] == '1':
                        b = u * n + v
                        union(a, b)
    if f == 0:
        return 0
    return len([1 for i in size if i == 1])



grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

print(numIslands(grid))


## dfs
def numIslands_dfs(grid):
    from collections import deque
    res = 0
    que = deque()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                que.append((i, j))
                grid[i][j] = '2'
                while que:
                    x, y = que.popleft()
                    if y > 0 and grid[x][y - 1] == '1':
                        que.append((x, y - 1))
                        grid[x][y - 1] = '2'
                    if x > 0 and grid[x - 1][y] == '1':
                        que.append((x - 1, y))
                        grid[x - 1][y] = '2'
                    if x < len(grid) - 1 and grid[x + 1][y] == '1':
                        que.append((x + 1, y))
                        grid[x + 1][y] = '2'
                    if y < len(grid[0]) - 1 and grid[x][y + 1] == '1':
                        que.append((x, y + 1))
                        grid[x][y + 1] = '2'
                res = res + 1
    return res






