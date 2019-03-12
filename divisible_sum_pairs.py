n,k = (int(x) for x in input().split())
array = list(map(int, input().split()))

count = 0
for i in range(len(array)-1):
    for x in range(1+i, len(array)):     
        if (array[i] + array[x]) % k == 0:
            count += 1
        
print(count)