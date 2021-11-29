

print('''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

Answer: 6857\n''')

import math

# n >= 2
def prim(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%2==0: return False
    return True

n = 600851475143
prims = []
for i in range(2,int(math.sqrt(n))+1):
    if prim(i): prims.append(i)

for i in prims:
    while n%i==0:
        n /= i
        ans = i
    if i>n: break

print(ans, '\n')

