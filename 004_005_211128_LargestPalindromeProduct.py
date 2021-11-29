

print('''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609\n''')

import math

def ans():
    for i in range(9,0,-1):
        for j in range(9,-1,-1):
            for k in range(9,-1,-1):
                n = 100001*i + 10010*j + 1100*k
                for l in range(100,int(math.sqrt(n))):
                    r = n//l
                    if (r<1000) and (l*r==n):
                        return n

# only considered 6-digit palindromes, but that's enough for this problem

print(ans(), '\n')

