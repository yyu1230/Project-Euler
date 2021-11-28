

print('''
Problem URL: https://projecteuler.net/problem=6

Answer: xxxxxx\n''')

n = 100

sumsqur = 0
for i in range(1,n+1):
    sumsqur += i*i

sqursum = (n*(n+1)/2)**2

ans = int(sqursum - sumsqur)

print(ans, '\n')

