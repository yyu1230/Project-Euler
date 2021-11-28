

print('''
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

Answer: 232792560\n''')

import math

# n >= 2
def prim(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n+.001)//i*i==n: return False
    return True

n = 20; ans = 1
for i in range(2,n+1):
    if prim(i): ans *= i**int(math.log(n,i))

print(ans, '\n')

