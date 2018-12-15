import sys

n = int(input().strip())
i = 1
while(i <= n):
    print((' ')*(n-i)+ ('#')*(i))
    i += 1
