

print('''
Using names.txt (https://projecteuler.net/project/resources/p022_names.txt), a
46K text file containing over five-thousand first names, begin by sorting it
into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.
For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?

Answer: 871198282\n''')

names = eval('['+open('p022_names.txt','r').read()+']')
n = 5163

names.sort()

ans = 0
for i in range(n):
    worth = 0
    for j in names[i]: worth += ord(j)-64
    ans += worth*(i+1)

print(ans, '\n')

