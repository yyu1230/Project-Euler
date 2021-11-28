

print('''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168\n''')

print('Method 1: Arithmetic')

n = 1000
num3 = (n-1)//3
num5 = (n-1)//5
num15 = (n-1)//15

print(3*num3*(num3+1)/2 + 5*num5*(num5+1)/2 - 15*num15*(num15+1)/2, '\n')


print('Method 2: Computational Brute Force')

ans = 0
for i in range(1000):
    if (i//3*3==i) or (i//5*5==i):
        ans += i

print(ans, '\n')

