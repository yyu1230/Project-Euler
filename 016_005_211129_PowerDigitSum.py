

print('''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

Answer: 1366\n''')

import math

n = 2**1000
ans = sum(int(i) for i in str(n))

print(ans, '\n')

