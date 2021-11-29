

print('''
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

Answer: 137846528820\n''')

n = 20

numRouts = [[1]*(n+1)]*(n+1)
for i in range(1,n+1):
    for j in range(1,n+1):
        numRouts[i][j] = numRouts[i][j-1] + numRouts[i-1][j]

ans = numRouts[n][n]

print(ans, '\n')

