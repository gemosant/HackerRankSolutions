def bon_appetit(n, k, cost, b):
    toplam = 0
    for i in cost:
        toplam += i
    if (b == ((toplam - cost[k]) // 2)):
        print('Bon Appetit')
    else:
        print(cost[k]//2)
        
#test_1
bon_appetit(3, 2, [2, 4, 6], 3)

#test_2
bon_appetit(3, 2, [2, 4, 6], 6)
