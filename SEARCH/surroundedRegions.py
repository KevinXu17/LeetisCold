## https://leetcode.com/problems/surrounded-regions/description/

def solve(board):
    from collections import deque
    xx = len(board)
    yy = len(board[0])
    que = deque()
    for x in range(xx):
        for y in range(yy):
            if (x == 0 or y == 0 or x == xx-1 or y == yy-1) and board[x][y] == 'O':
                que.append((x, y))
                board[x][y] = 'Y'
                while que:
                    m, n = que.popleft()
                    if m - 1 >= 0 and board[m - 1][n] == 'O':
                        que.append((m - 1, n))
                        board[m - 1][n] = 'Y'
                    if m + 1 < xx and board[m + 1][n] == 'O':
                        que.append((m + 1, n))
                        board[m + 1][n] = 'Y'
                    if n - 1 >= 0 and board[m][n - 1] == 'O':
                        que.append((m, n - 1))
                        board[m][n - 1] = 'Y'
                    if n + 1 < yy and board[m][n + 1] == 'O':
                        que.append((m, n + 1))
                        board[m][n + 1] = 'Y'
    for x in range(xx):
        for y in range(yy):
            if board[x][y] == 'O':
                board[x][y] = 'X'
            elif board[x][y] == 'Y':
                board[x][y] = 'O'


b = [["O","X","X","O","X"],
     ["X","O","O","X","O"],
     ["X","O","X","O","X"],
     ["O","X","O","O","O"],
     ["X","X","O","X","O"]]
solve(b)
for x in range(len(b)):
    for y in range(len(b[0])):
        print(b[x][y] + ' ')