

print('''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Answer: 142913828922\n''')

import math

# n >= 2
def prim(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

ans = 0
for i in range(2,int(2e6)+1):
    if prim(i): ans += i

print(ans, '\n')

