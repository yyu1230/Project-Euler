

print('''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.
What is the 10 001st prime number?

Answer: 104743\n''')

import math

# n >= 2
def prim(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n+.001)//i*i==n: return False
    return True

ans = 1; no = 0
while True:
    ans += 1
    if prim(ans): no += 1
    if no==10001: break

print(ans, '\n')

