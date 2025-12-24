N = int(input())
M = int(input())
grid = [[0 for _ in range(N)] for _ in range(N)]

for i in range(M):
    print({i+1})
    r1 = int(input())
    c1 = int(input())
    r2 = int(input())
    c2 = int(input())
    color = int(input())
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if grid[r][c] == 0:
                grid[r][c] = color
            elif grid[r][c] != color and grid[r][c] != 3:
                grid[r][c] = 3
color_to_find = int(input())
count = 0
for row in grid:
    count += row.count(color_to_find)
print(count)