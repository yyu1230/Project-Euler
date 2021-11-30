

print('''
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.
Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

Answer: 4179871\n''')

numbrs = list(range(1,28124))

def sumPDiv(n):
    spd = 0
    for i in range(1,(n//2)+1):
        if n%i==0: spd += i
    return spd

abundnt = []
for i in range(2,28123):
    if sumPDiv(i)>i: abundnt.append(i)

lenAbdt = len(abundnt)
for i in range(lenAbdt):
    for j in range(i,lenAbdt):
        sumIJ = abundnt[i]+abundnt[j]
        if sumIJ>28123: break
        numbrs[sumIJ-1] = 0

ans = sum(numbrs)

print(ans, '\n')

