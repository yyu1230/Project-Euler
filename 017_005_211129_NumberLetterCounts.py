

print('''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-
two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

Answer: 21124\n''')

cardnl = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8, 6, 6, 5, 5,
          5, 7, 6, 6, 7, 8]
# length of numbers [1-20], [30, 40, 50, ..., 90], [hundred, thousand]
# indices in cardnl [0-19], [20, 21, 22, ..., 26], [27,      28]

def numLettrs(n):
    if n==1000: return cardnl[0] + cardnl[28]
    if n%100==0: return cardnl[n//100-1] + cardnl[27]
    if n>100: return cardnl[n//100-1] + cardnl[27] + 3 + numLettrs(n%100)
    if n<=20: return cardnl[n-1]
    if n%10==0: return cardnl[n//10+17]
    return cardnl[n//10+17] + cardnl[n%10-1]

ans = 0
for i in range(1,1001): ans += numLettrs(i)

print(ans, '\n')

