

print('''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer: 31875000\n''')

import math

print('''Mathematical thought process:
Note: a < b < c
Substitute a = 1,000-b-c into a^2 = c^2 - b^2, we get (after a series of
algebraic manipulation)
b(b+c) - 1,000(b+c) + 500,000 = 0
Let d = b + c, we get
d * (1,000-b) = 500,000
Because d=b+c and 1,000-b=a+c, we get 1,000-b < d, both between (500,1000)
''')

n = 500000
for d in range(int(math.sqrt(n)),1000):
    if n%d: continue
    a = 1000 - d; b = 1000 - n//d; c = d - b
    if a*a+b*b==c*c: break

ans = a*b*c

print(ans, '\n')

