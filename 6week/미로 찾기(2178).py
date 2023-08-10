n, m = map(int, input().split())
maze = []

for _ in range(n):
    tmp = int(input())
    data = []
    for i in range(m):
        data.insert(0, tmp % 10)
        tmp //= 10
    maze.append(data)

dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1, 1]

queue = [[0, 0]]

while queue:
    x, y = queue[0][0], queue[0][1]
    del queue[0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
            queue.append([nx, ny])
            maze[nx][ny] = maze[x][y] + 1

print(maze[n-1][m-1])
