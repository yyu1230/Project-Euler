

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
Substitute a = 1,000-b-c into a^2 = c^2 - b^2, we get (after a series of algebraic manipulation)
b(b+c) - 1,000(b+c) + 500,000 = 0
Let x = b, y = b + c, we get
y * (1,000-x) = 500,000
Because y=a+b and 1,000-x=a+c, y < 1,000-x, both between (500,1000)
''')

n = 500000
for y in range(501,int(math.sqrt(n))):
    if (n+.001)//y*y!=n: continue
    x = 1000 - n//y
    b = x
    c = y - x
    a = 1000 - y
    if a*a+b*b==c*c: break

ans = a*b*c

print(ans, '\n')

