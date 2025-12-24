N = int(input())
M = int(input())
grid = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):
    print({i+1})
    r = int(input())
    c = int(input())
    s = int(input())
    grid[r][c] = 1
    for k in range(1, s + 1):
        if r - k >= 0: grid[r-k][c] = 1
        if r + k < N:  grid[r+k][c] = 1
        if c - k >= 0: grid[r][c-k] = 1
        if c + k < N:  grid[r][c+k] = 1
count_zero = 0
for row in grid:
    count_zero += row.count(0)
print(count_zero)