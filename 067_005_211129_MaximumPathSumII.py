

print('''
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt (https://projecteuler.
net/project/resources/p067_triangle.txt), a 15K text file containing a triangle
with one-hundred rows.
NOTE: This is a much more difficult version of Problem 18. It is not possible to
try every route to solve this problem, as there are 299 altogether! If you could
check one trillion (1012) routes every second it would take over twenty billion
years to check them all. There is an efficient algorithm to solve it. ;o)

Answer: 7273\n''')

tringlstr = open('p067_triangle.txt', 'r').read()

n = 100

def tringl(i,j): return int(tringlstr [i*(i+1)*3//2+j*3: i*(i+1)*3//2+j*3+2])

maxTotl = []
for i in range(n): maxTotl.append([])
for i in range(n):
    for j in range(i+1): maxTotl[i].append(0)

maxTotl[0][0] = tringl(0,0)
for i in range(1,n):
    maxTotl[i][0] = tringl(i,0) + maxTotl[i-1][0]
    maxTotl[i][i] = tringl(i,i) + maxTotl[i-1][i-1]
for i in range(2,n):
    for j in range(1,i):
        maxTotl[i][j] = tringl(i,j) + max(maxTotl[i-1][j],maxTotl[i-1][j-1])

ans = 0
for i in range(n):
    if ans<maxTotl[n-1][i]: ans = maxTotl[n-1][i]

print(ans, '\n')

